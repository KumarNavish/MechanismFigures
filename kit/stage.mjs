// MechanismFigures stage: a small, opinionated three.js studio for 3D mechanism figures.
// Orthographic camera, z-up world, soft contact shadows, crease and silhouette outlines,
// capped cutaways, exploded parts with tethers, and vector labels that stay editable.
// Use it through `node scripts/render.mjs figure.mjs`. See references/stage.md.
import * as THREE from 'three';
import {Line2} from 'three/addons/lines/Line2.js';
import {LineGeometry} from 'three/addons/lines/LineGeometry.js';
import {LineSegments2} from 'three/addons/lines/LineSegments2.js';
import {LineSegmentsGeometry} from 'three/addons/lines/LineSegmentsGeometry.js';
import {LineMaterial} from 'three/addons/lines/LineMaterial.js';

export {THREE};
THREE.Object3D.DEFAULT_UP.set(0, 0, 1);

const PX = 96 / 25.4; // CSS pixels per millimetre
const NS = 'http://www.w3.org/2000/svg';

// One colour, one meaning. Context is a pale cool tone, never grey; `focus` is the operation; `act` is the intervention.
export const palette = {
  ink: '#16263f', line: '#24385a', context: '#cfe1f5', quiet: '#e8f1fb', paper: '#ffffff', shade: '#2f4f86',
  focus: '#2b6fdb', act: '#ee7b1f', good: '#259b6c', warn: '#c9362c', violet: '#7657c9', gold: '#d9a514',
};
export const ramps = {
  viridis: ['#440154', '#414487', '#2a788e', '#22a884', '#7ad151', '#fde725'],
  magma: ['#0b0724', '#3b0f70', '#8c2981', '#de4968', '#fe9f6d', '#fcfdbf'],
  diverging: ['#2b6fdb', '#a9c4ee', '#e6eefb', '#f6c9a3', '#d9541e'], // zero is the middle stop
};
/** ramp(stops) returns t in [0,1] -> THREE.Color. Use one ramp for one quantity in all panels. */
export function ramp(stops = ramps.viridis) {
  const cs = stops.map(s => new THREE.Color(s));
  return t => {
    const x = Math.min(1, Math.max(0, Number.isFinite(t) ? t : 0)) * (cs.length - 1);
    const i = Math.min(cs.length - 2, Math.floor(x));
    return cs[i].clone().lerp(cs[i + 1], x - i);
  };
}
const V = p => (p && p.isVector3) ? p.clone() : new THREE.Vector3(p[0], p[1], p[2] ?? 0);

export function createStage(opts = {}) {
  const o = {width: 180, height: 110, azim: -50, elev: 28, margin: 8, zoom: 1, shift: [0, 0], fov: 0,
    background: '#ffffff', ground: true, shadow: 0.16, edgeWidth: 0.28, font: 'Helvetica Neue, Helvetica, Arial, sans-serif',
    minFont: 6.5, mount: document.body, ...opts};
  const W = Math.round(o.width * PX), H = Math.round(o.height * PX);
  const renderer = new THREE.WebGLRenderer({antialias: true, alpha: true, stencil: true, preserveDrawingBuffer: true});
  renderer.setPixelRatio(window.devicePixelRatio || 1);
  renderer.setSize(W, H);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.VSMShadowMap;
  renderer.localClippingEnabled = true;
  renderer.setClearColor(o.background, 1);
  o.mount.style.cssText += `;position:relative;width:${W}px;height:${H}px`;
  o.mount.appendChild(renderer.domElement);
  const svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('xmlns', NS);
  svg.setAttribute('viewBox', `0 0 ${o.width} ${o.height}`);
  svg.setAttribute('width', W); svg.setAttribute('height', H);
  svg.style.cssText = 'position:absolute;left:0;top:0';
  o.mount.appendChild(svg);

  const scene = new THREE.Scene();
  const a = THREE.MathUtils.degToRad(o.azim), e = THREE.MathUtils.degToRad(o.elev);
  const eyeDir = new THREE.Vector3(Math.cos(e) * Math.cos(a), Math.cos(e) * Math.sin(a), Math.sin(e));
  const camera = o.fov ? new THREE.PerspectiveCamera(o.fov, W / H, 0.01, 1e4) : new THREE.OrthographicCamera(-1, 1, 1, -1, 0.01, 1e4);
  camera.position.copy(eyeDir); camera.lookAt(0, 0, 0); camera.updateMatrixWorld();
  const camRight = new THREE.Vector3().setFromMatrixColumn(camera.matrixWorld, 0);
  const camUp = new THREE.Vector3().setFromMatrixColumn(camera.matrixWorld, 1);

  let cutOrder = 0;
  const lineMats = [], labels = [], overlays = [], hulls = [], cuts = [], dashed = [];
  const lineMat = (color, widthMm, extra = {}) => {
    const m = new LineMaterial({color: new THREE.Color(color), linewidth: widthMm * PX, ...extra});
    m.resolution.set(W, H); lineMats.push(m); return m;
  };
  const S = {THREE, scene, camera, renderer, svg, palette, options: o};

  /** World vector for `d` units toward screen right / screen up. Translate copies with these to make
   *  fixed-camera small multiples: an orthographic camera shows each copy from the identical view. */
  S.right = (d = 1) => camRight.clone().multiplyScalar(d);
  S.up = (d = 1) => camUp.clone().multiplyScalar(d);
  S.toward = (d = 1) => eyeDir.clone().multiplyScalar(d);

  /** Add a mesh from any THREE geometry with the house look.
   *  opts: color, opacity (below 1 makes a ghost), edges (crease lines), outline (silhouette),
   *  flat, roughness, metalness, side, vertexColors, id (name used in the audit),
   *  shadow:false (no shadow from or on this part), receive:false (casts on the ground, takes no shadow:
   *  use it for cells and surfaces whose tone is data), unlit:true (exact colour, no shading: use it
   *  when the reader must read a value from the colour). */
  S.solid = (geometry, p = {}) => {
    const q = {color: palette.context, opacity: 1, edges: true, outline: true, flat: false, roughness: 0.72,
      metalness: 0, edgeColor: palette.line, edgeWidth: o.edgeWidth, ...p};
    const ghost = q.opacity < 1;
    const common = {color: q.color, transparent: ghost, opacity: q.opacity, depthWrite: !ghost, vertexColors: !!q.vertexColors,
      side: q.side ?? (ghost ? THREE.DoubleSide : THREE.FrontSide)};
    // unlit: the drawn colour is exactly the given colour. Light and shadow do not change it.
    const mat = q.unlit ? new THREE.MeshBasicMaterial(common)
      : new THREE.MeshStandardMaterial({...common, roughness: q.roughness, metalness: q.metalness, flatShading: q.flat});
    const mesh = new THREE.Mesh(geometry, mat);
    // With the soft shadow map, a mesh that receives shadow also casts. Thus shadow:false stops both.
    mesh.castShadow = q.shadow ?? !ghost; mesh.receiveShadow = q.receive ?? (q.shadow !== false && !ghost && !q.vertexColors && !q.unlit);
    if (ghost) mesh.renderOrder = 5;
    mesh.name = q.id || '';
    if (q.edges) {
      const eg = new THREE.EdgesGeometry(geometry, q.edgeAngle ?? 28);
      if (eg.attributes.position.count) {
        const seg = new LineSegments2(new LineSegmentsGeometry().setPositions(eg.attributes.position.array),
          lineMat(q.edgeColor, q.edgeWidth * (ghost ? 0.7 : 1), ghost ? {transparent: true, opacity: 0.55, depthWrite: false} : {}));
        seg.userData.helper = true; seg.renderOrder = ghost ? 6 : 1; mesh.add(seg);
      }
    }
    if (q.outline && !ghost) hulls.push({mesh, color: q.edgeColor, width: q.edgeWidth});
    (q.parent || scene).add(mesh);
    return mesh;
  };
  const orient = (obj, from, to) => {
    const d = V(to).sub(V(from)), L = d.length();
    obj.position.copy(V(from).add(V(to)).multiplyScalar(0.5));
    obj.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.normalize());
    return L;
  };
  S.box = (center, size, p) => { const m = S.solid(new THREE.BoxGeometry(...size), p); m.position.copy(V(center)); return m; };
  S.sphere = (center, r, p) => { const m = S.solid(new THREE.SphereGeometry(r, 64, 40), {edges: false, ...p}); m.position.copy(V(center)); return m; };
  /** Cylinder or cone from point a to point b. p.r2 sets the radius at b. */
  S.cyl = (from, to, r, p = {}) => {
    const L = V(to).distanceTo(V(from));
    const m = S.solid(new THREE.CylinderGeometry(p.r2 ?? r, r, L, p.segments ?? 64, 1, !!p.open), p);
    orient(m, from, to); return m;
  };
  /** Solid 3D arrow: a force, flow, displacement or ray. Depth-correct, unlike an overlay arrow. */
  S.arrow = (from, to, p = {}) => {
    const q = {color: palette.focus, radius: 0.02, head: 3.2, edges: false, outline: false, shadow: false, ...p};
    const A = V(from), B = V(to), L = A.distanceTo(B), hl = Math.min(L * 0.6, q.radius * q.head * 2.4);
    const mid = A.clone().lerp(B, 1 - hl / L), g = new THREE.Group();
    S.cyl(A, mid, q.radius, {...q, parent: g}); S.cyl(mid, B, q.radius * q.head, {...q, r2: 0, parent: g});
    scene.add(g); return g;
  };
  /** Smooth tube through points: a fibre, vessel, path or streamline with real depth. */
  S.tube = (points, p = {}) => {
    const q = {radius: 0.02, color: palette.focus, closed: false, edges: false, ...p};
    const c = new THREE.CatmullRomCurve3(points.map(V), q.closed, 'centripetal');
    return S.solid(new THREE.TubeGeometry(c, Math.max(32, points.length * 12), q.radius, 16, q.closed), q);
  };
  /** Constant-width line through points. width is in mm on the page. p.dash is in world units. */
  S.curve = (points, p = {}) => {
    const q = {color: palette.ink, width: 0.35, ...p};
    const g = new LineGeometry().setPositions(points.flatMap(x => V(x).toArray()));
    const m = lineMat(q.color, q.width, q.dash ? {dashed: true, dashSize: q.dash, gapSize: q.gap ?? q.dash * 0.7} : {});
    if (q.opacity != null) { m.transparent = true; m.opacity = q.opacity; }
    const l = new Line2(g, m); l.computeLineDistances(); l.userData.helper = true; l.renderOrder = 2;
    (q.parent || scene).add(l); return l;
  };
  /** Parametric surface f(u,v) -> [x,y,z], u and v in [0,1]. p.value(u,v,point) with p.ramp paints a field. */
  S.surface = (f, p = {}) => {
    const q = {nu: 96, nv: 96, color: palette.context, edges: false, outline: false, side: THREE.DoubleSide, ...p};
    const pos = [], col = [], idx = [], rp = q.value ? ramp(q.ramp) : null, [lo, hi] = q.range || [0, 1];
    for (let j = 0; j <= q.nv; j++) for (let i = 0; i <= q.nu; i++) {
      const u = i / q.nu, v = j / q.nv, P = f(u, v); pos.push(P[0], P[1], P[2]);
      if (rp) { const c = rp((q.value(u, v, P) - lo) / (hi - lo)); col.push(c.r, c.g, c.b); }
    }
    for (let j = 0; j < q.nv; j++) for (let i = 0; i < q.nu; i++) {
      const k = j * (q.nu + 1) + i; idx.push(k, k + 1, k + q.nu + 2, k, k + q.nu + 2, k + q.nu + 1);
    }
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
    if (rp) g.setAttribute('color', new THREE.Float32BufferAttribute(col, 3));
    g.setIndex(idx); g.computeVertexNormals();
    return S.solid(g, {...q, color: rp ? '#ffffff' : q.color, vertexColors: !!rp});
  };
  /** Translucent reference or section plane through `point` with unit `normal`. */
  S.plane = (point, normal, size = [1, 1], p = {}) => {
    const m = S.solid(new THREE.PlaneGeometry(size[0], size[1]), {color: palette.focus, opacity: 0.16, edges: true, ...p});
    m.position.copy(V(point)); m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 0, 1), V(normal).normalize());
    return m;
  };
  /** Move a part out of the assembly by `offset` and leave a dashed tether to where it belongs. */
  S.explode = (obj, offset, p = {}) => {
    const from = new THREE.Box3().setFromObject(obj).getCenter(new THREE.Vector3());
    obj.position.add(V(offset));
    if (p.tether !== false) dashed.push(S.curve([from, from.clone().add(V(offset))], {color: palette.line, width: 0.22, dash: 1, opacity: 0.8}));
    return obj;
  };
  /** Cut objects with a plane and cap the cut. `normal` points to the side that is REMOVED.
   *  cap: colour of the section face, or false for thin open shells (their inside then shows). */
  S.cut = (objects, point, normal, p = {}) => {
    const n = V(normal).normalize().negate();
    const plane = new THREE.Plane().setFromNormalAndCoplanarPoint(n, V(point));
    cuts.push(plane);
    [].concat(objects).forEach(root => root.traverse(m => {
      if (m.userData.stencil || m.userData.cap) return;
      if (m.material) {
        m.material.clippingPlanes = [...(m.material.clippingPlanes || []), plane]; m.material.clipShadows = true;
        m.material.clipIntersection = m.material.clippingPlanes.length > 1;   // two cuts remove a quarter, not three quarters
      }
      if (!m.isMesh || m.userData.helper) return;
      m.material.side = THREE.DoubleSide;
      if (p.cap === false) return;
      const order = 10 + (++cutOrder);
      for (const [side, op] of [[THREE.BackSide, THREE.IncrementWrapStencilOp], [THREE.FrontSide, THREE.DecrementWrapStencilOp]]) {
        const sm = new THREE.Mesh(m.geometry, new THREE.MeshBasicMaterial({depthWrite: false, depthTest: false, colorWrite: false,
          stencilWrite: true, stencilFunc: THREE.AlwaysStencilFunc, side, clippingPlanes: [plane],
          stencilFail: op, stencilZFail: op, stencilZPass: op}));
        sm.renderOrder = order; sm.userData.stencil = sm.userData.helper = true; m.add(sm);
      }
      const capColor = p.cap || new THREE.Color(m.material.color).offsetHSL(0, 0.15, -0.2); // darker and more saturated, not greyer
      const cap = new THREE.Mesh(new THREE.PlaneGeometry(1e3, 1e3), new THREE.MeshStandardMaterial({color: capColor, roughness: 0.9,
        stencilWrite: true, stencilRef: 0, stencilFunc: THREE.NotEqualStencilFunc,
        stencilFail: THREE.ReplaceStencilOp, stencilZFail: THREE.ReplaceStencilOp, stencilZPass: THREE.ReplaceStencilOp, side: THREE.DoubleSide}));
      cap.position.copy(V(point)); cap.quaternion.setFromUnitVectors(new THREE.Vector3(0, 0, 1), n);
      cap.renderOrder = order + 0.5; cap.onAfterRender = r => r.clearStencil();
      cap.userData.helper = cap.userData.nofit = cap.userData.cap = true; scene.add(cap);
      (m.userData.caps = m.userData.caps || []).push({cap, plane});
      // Each cap shows only inside the region that the other cuts of this object remove.
      for (const k of m.userData.caps) k.cap.material.clippingPlanes = m.userData.caps.filter(x => x !== k).map(x => x.plane.clone().negate());
    }));
    return plane;
  };

  /** Vector label with a leader from a 3D anchor. dx, dy in mm (screen). Text stays editable in the SVG. */
  S.label = (anchor, text, p = {}) => { labels.push({anchor: V(anchor), text, dx: 7, dy: -6, size: 8, leader: true, color: palette.ink, ...p}); };
  /** 2D text at page position in mm. Use for panel letters, state names and equations. */
  S.text = (x, y, text, p = {}) => { overlays.push({kind: 'text', x, y, text, size: 8, color: palette.ink, ...p}); };
  /** 2D overlay arrow between two places; each end is a 3D point or [x, y] in mm. Narrative only: it has no depth. */
  S.link = (from, to, p = {}) => { overlays.push({kind: 'link', from, to, color: palette.ink, width: 0.35, bend: 0, ...p}); };

  const project = P => { const v = V(P).project(camera); return [(v.x + 1) / 2 * o.width, (1 - v.y) / 2 * o.height]; };
  S.project = project;
  const el = (name, attrs, parent = svg) => { const n = document.createElementNS(NS, name); for (const k in attrs) n.setAttribute(k, attrs[k]); parent.appendChild(n); return n; };
  const pt = s => s * 25.4 / 72; // points -> mm (viewBox units)
  const textEl = (x, y, t, q) => {
    const n = el('text', {x: x.toFixed(2), y: y.toFixed(2), 'font-family': o.font, 'font-size': pt(q.size).toFixed(3), fill: q.color,
      'font-weight': q.weight || 400, 'font-style': q.italic ? 'italic' : 'normal', 'text-anchor': q.align || 'start',
      stroke: o.background, 'stroke-width': q.halo ?? 0.7, 'stroke-linejoin': 'round', 'paint-order': 'stroke', 'data-mf-label': '1'});
    String(t).split('\n').forEach((line, i) => { const s = el('tspan', {x: x.toFixed(2), dy: i ? '1.2em' : 0}, n); s.textContent = line; });
    return n;
  };

  /** Fit the camera, light the scene, render, draw labels and audit. Call once, last. */
  S.done = () => {
    scene.updateMatrixWorld(true);
    const box = new THREE.Box3();
    scene.traverse(m => { if ((m.isMesh || m.isLine2 || m.isLineSegments2) && !m.userData.nofit && !m.userData.stencil) box.expandByObject(m); });
    if (box.isEmpty()) box.set(new THREE.Vector3(-1, -1, -1), new THREE.Vector3(1, 1, 1));
    const floor = box.min.z;
    // A fixed frame keeps the identical camera in every beat of a sequence, whatever each beat contains.
    if (o.frame) box.setFromCenterAndSize(V(o.frame.center || [0, 0, 0]), V(o.frame.size));
    const c = box.getCenter(new THREE.Vector3()), R = box.getSize(new THREE.Vector3()).length() / 2 || 1;
    camera.position.copy(c).addScaledVector(eyeDir, R * (o.fov ? 1.15 / Math.tan(THREE.MathUtils.degToRad(o.fov) / 2) : 4));
    camera.near = R * 0.05; camera.far = R * 12; camera.lookAt(c); camera.updateMatrixWorld();
    if (!o.fov) {
      let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
      for (let i = 0; i < 8; i++) {
        const q = new THREE.Vector3(i & 1 ? box.max.x : box.min.x, i & 2 ? box.max.y : box.min.y, i & 4 ? box.max.z : box.min.z).applyMatrix4(camera.matrixWorldInverse);
        x0 = Math.min(x0, q.x); x1 = Math.max(x1, q.x); y0 = Math.min(y0, q.y); y1 = Math.max(y1, q.y);
      }
      const s = Math.max((x1 - x0) / (o.width - 2 * o.margin), (y1 - y0) / (o.height - 2 * o.margin)) / o.zoom; // world units per mm
      const cx = (x0 + x1) / 2 - o.shift[0] * s, cy = (y0 + y1) / 2 + o.shift[1] * s;
      camera.left = cx - o.width * s / 2; camera.right = cx + o.width * s / 2;
      camera.top = cy + o.height * s / 2; camera.bottom = cy - o.height * s / 2;
      S.unitsPerMm = s;
    }
    camera.updateProjectionMatrix();
    const upm = S.unitsPerMm || R / 40;
    for (const d of dashed) { d.material.dashSize *= upm * 1.2; d.material.gapSize *= upm * 1.2; }

    // Light: one key from the upper left of the VIEW, a broad fill, and a ground that only catches shadow.
    scene.add(new THREE.HemisphereLight(0xffffff, 0xcfe1f5, 1.9));
    const key = new THREE.DirectionalLight(0xffffff, 1.9);
    key.position.copy(c).addScaledVector(camRight, -0.75 * R * 3).addScaledVector(camUp, 1.1 * R * 3).addScaledVector(eyeDir, 0.9 * R * 3);
    if (key.position.z < c.z + R) key.position.z = c.z + R * 2;
    key.target.position.copy(c); scene.add(key, key.target);
    key.castShadow = true; key.shadow.mapSize.set(4096, 4096); key.shadow.radius = 9; key.shadow.blurSamples = 25;
    key.shadow.bias = -0.0004; key.shadow.normalBias = R * 0.004;
    Object.assign(key.shadow.camera, {left: -R * 1.6, right: R * 1.6, top: R * 1.6, bottom: -R * 1.6, near: 0.01, far: R * 12});
    const fill = new THREE.DirectionalLight(0xffffff, 0.55);
    fill.position.copy(c).addScaledVector(camRight, R * 3).addScaledVector(eyeDir, R * 2); scene.add(fill);
    if (o.ground !== false && o.shadow > 0) {
      const g = new THREE.Mesh(new THREE.PlaneGeometry(R * 40, R * 40), new THREE.ShadowMaterial({opacity: o.shadow, color: new THREE.Color(o.shadowColor || palette.shade)}));
      g.position.set(c.x, c.y, (typeof o.ground === 'number' ? o.ground : floor) - R * 1e-3);
      g.receiveShadow = true; g.userData.helper = g.userData.nofit = true; scene.add(g);
    }
    // Silhouette outline: a back-face hull pushed out by the line width. Creases come from EdgesGeometry.
    for (const h of hulls) {
      const g = h.mesh.geometry.clone();
      if (!g.attributes.normal) g.computeVertexNormals();
      const P = g.attributes.position, N = g.attributes.normal, t = h.width * upm * 0.9;
      const sc = new THREE.Vector3().setFromMatrixScale(h.mesh.matrixWorld);
      for (let i = 0; i < P.count; i++) P.setXYZ(i, P.getX(i) + N.getX(i) * t / sc.x, P.getY(i) + N.getY(i) * t / sc.y, P.getZ(i) + N.getZ(i) * t / sc.z);
      const hm = new THREE.Mesh(g, new THREE.MeshBasicMaterial({color: h.color, side: THREE.BackSide, clippingPlanes: h.mesh.material.clippingPlanes || [], clipIntersection: h.mesh.material.clipIntersection}));
      hm.userData.helper = hm.userData.nofit = true; h.mesh.add(hm);
    }
    renderer.render(scene, camera);

    // Vector overlay.
    el('rect', {x: 0, y: 0, width: o.width, height: o.height, fill: 'none', 'data-mf-frame': '1'});
    const mk = el('defs', {});
    const audit = {warnings: [], labels: labels.length, meshes: 0, unitsPerMm: +upm.toFixed(5)};
    const targets = [];
    scene.traverse(m => { if (m.isMesh && !m.userData.helper && m.material.opacity >= 0.5) { targets.push(m); audit.meshes++; } });
    const ray = new THREE.Raycaster();
    const end = (P, i) => Array.isArray(P) && P.length === 2 ? P : project(P);
    overlays.forEach((v, i) => {
      if (v.kind === 'text') return textEl(v.x, v.y, v.text, v);
      const A = end(v.from), B = end(v.to), id = 'mf-arrow-' + i;
      const m = el('marker', {id, viewBox: '0 0 10 10', refX: 8.5, refY: 5, markerWidth: 5.5, markerHeight: 5.5, orient: 'auto-start-reverse'}, mk);
      el('path', {d: 'M0 1 L10 5 L0 9 z', fill: v.color}, m);
      const mx = (A[0] + B[0]) / 2 - (B[1] - A[1]) * v.bend, my = (A[1] + B[1]) / 2 + (B[0] - A[0]) * v.bend;
      el('path', {d: `M${A[0].toFixed(2)} ${A[1].toFixed(2)} Q${mx.toFixed(2)} ${my.toFixed(2)} ${B[0].toFixed(2)} ${B[1].toFixed(2)}`, fill: 'none', stroke: v.color,
        'stroke-width': v.width, 'stroke-dasharray': v.dash || 'none', 'marker-end': `url(#${id})`, 'stroke-linecap': 'round'});
      if (v.text) { // on the curve midpoint, moved 2 mm off the line toward the outside of the bend
        const cx = (A[0] + 2 * mx + B[0]) / 4, cy = (A[1] + 2 * my + B[1]) / 4, L = Math.hypot(B[0] - A[0], B[1] - A[1]) || 1, side = v.bend > 0 ? 1 : -1;
        textEl(cx - (B[1] - A[1]) / L * 2 * side, cy + (B[0] - A[0]) / L * 2 * side + 1, v.text, {size: 7.5, align: 'middle', ...v, color: v.textColor || v.color});
      }
    });
    const boxes = [];
    for (const L of labels) {
      const [x, y] = project(L.anchor), tx = x + L.dx, ty = y + L.dy;
      const origin = L.anchor.clone().addScaledVector(eyeDir, R * 6);
      ray.set(origin, eyeDir.clone().negate());
      const hit = ray.intersectObjects(targets, false).find(h => !cuts.some(pl => (h.object.material.clippingPlanes || []).includes(pl) && pl.distanceToPoint(h.point) < 0));
      if (!o.fov && hit && hit.distance < R * 6 - R * 0.02) audit.warnings.push(`label "${L.text}": its anchor is hidden behind ${hit.object.name || 'another object'}; move the anchor to a visible point`);
      const align = L.align || (L.dx < -1 ? 'end' : L.dx > 1 ? 'start' : 'middle');
      if (L.leader && Math.hypot(L.dx, L.dy) > 2.5) {
        const k = 1 - 1.4 / Math.hypot(L.dx, L.dy);
        el('line', {x1: x.toFixed(2), y1: y.toFixed(2), x2: (x + L.dx * k).toFixed(2), y2: (y + L.dy * k).toFixed(2), stroke: L.color, 'stroke-width': 0.22});
        el('circle', {cx: x.toFixed(2), cy: y.toFixed(2), r: 0.5, fill: L.color, stroke: o.background, 'stroke-width': 0.18});
      }
      const n = textEl(tx, ty + (L.dy > 1 ? pt(L.size) * 0.75 : L.dy < -1 ? -0.4 : pt(L.size) * 0.35), L.text, {...L, align});
      boxes.push({node: n, text: L.text, b: n.getBBox(), size: L.size});
    }
    svg.querySelectorAll('text').forEach(n => { if (!boxes.some(b => b.node === n)) boxes.push({node: n, text: n.textContent, b: n.getBBox(), size: parseFloat(n.getAttribute('font-size')) * 72 / 25.4}); });
    boxes.forEach((p, i) => {
      if (p.size < o.minFont) audit.warnings.push(`text "${String(p.text).replace(/\n/g, " ")}": ${p.size.toFixed(1)} pt is below the ${o.minFont} pt minimum`);
      if (p.b.x < 0 || p.b.y < 0 || p.b.x + p.b.width > o.width || p.b.y + p.b.height > o.height) audit.warnings.push(`text "${String(p.text).replace(/\n/g, " ")}" leaves the frame`);
      for (let j = i + 1; j < boxes.length; j++) { const q = boxes[j].b; if (p.b.x < q.x + q.width && q.x < p.b.x + p.b.width && p.b.y < q.y + q.height && q.y < p.b.y + p.b.height) audit.warnings.push(`text "${String(p.text).replace(/\n/g, " ")}" overlaps "${boxes[j].text}"`); }
    });
    audit.note = 'The audit finds hidden anchors, clipped, small and overlapping text only. Look at every PNG yourself.';
    window.__mf = {audit, width: o.width, height: o.height, raster: renderer.domElement.toDataURL('image/png'), overlay: svg.innerHTML};
    return audit;
  };
  return S;
}
