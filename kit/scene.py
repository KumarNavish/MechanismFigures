"""Evidence-linked SVG primitives with inspectable identity and geometry.

No invented data, layout engine, text measurement, automatic scientific scoring,
3D collision proof, or forced isometric style. Keep the scientific model separate.
"""
import html
import json
import math
import re
from pathlib import Path
from .geometry import point

KINDS = {'formal','measured','inferred','simulated','schematic'}
COLORS = {'active':'#364c73','context':'#8a919d','intervention':'#a56342','ink':'#20252b','paper':'#ffffff'}


def finite(value, positive=False):
    if type(value) not in (int,float) or not math.isfinite(value) or (positive and value<=0):
        raise ValueError('Expected finite '+('positive ' if positive else '')+'number')
    return value


def paint(value):
    result=COLORS.get(value,value)
    if not isinstance(result,str) or not re.fullmatch(r'#[a-fA-F0-9]{6}|none',result):
        raise ValueError('Use a named semantic role or a six-digit hex color')
    return result


class Scene:
    def __init__(self, title, description, width_mm=180, height_mm=110, units_per_mm=6, min_font_pt=7):
        if not title.strip() or not description.strip():raise ValueError('Title and evidence-aware description required')
        self.width_mm=finite(width_mm,True);self.height_mm=finite(height_mm,True)
        self.unit=finite(units_per_mm,True);self.min_font=finite(min_font_pt,True)
        self.width=self.width_mm*self.unit;self.height=self.height_mm*self.unit
        self.title=title;self.description=description;self.parts=[];self.marks={};self.anchors={}

    def _record(self, name, meaning, evidence, status, kind, bounds):
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*',name) or name in self.marks:
            raise ValueError('Each mark needs a unique safe stable ID')
        if not isinstance(meaning,str) or not meaning.strip():raise ValueError('Explain what this mark means')
        if not isinstance(evidence,(list,tuple)) or not evidence or any(not isinstance(e,str) or not e.strip() for e in evidence):
            raise ValueError('Declare evidence IDs, including for a labeled schematic')
        if status not in KINDS:raise ValueError('Unknown evidential status')
        self.marks[name]={'id':name,'kind':kind,'meaning':meaning,'evidence_ids':list(evidence),'status':status,'bounds':bounds}
        return 'id="{}" data-mf-mark="{}" data-mf-status="{}"'.format(name,kind,status)

    def anchor(self, name, xy, owner):
        if name in self.anchors or owner not in self.marks:raise ValueError('Anchor needs a unique name and existing owner')
        self.anchors[name]={'point':point(xy),'owner':owner}
        return name

    def circle(self,name,center,radius,*,meaning,evidence,status='schematic',fill='active',stroke='ink'):
        x,y=point(center);r=finite(radius,True)
        attrs=self._record(name,meaning,evidence,status,'circle',[x-r,y-r,x+r,y+r])
        self.parts.append('<circle {} cx="{}" cy="{}" r="{}" fill="{}" stroke="{}" stroke-width="1.5"/>'.format(attrs,x,y,r,paint(fill),paint(stroke)))
        return self

    def polygon(self,name,points,*,meaning,evidence,status='schematic',fill='active',stroke='ink'):
        pts=[point(p) for p in points]
        if len(pts)<3:raise ValueError('A polygon needs at least three points')
        area=sum(x*pts[(i+1)%len(pts)][1]-y*pts[(i+1)%len(pts)][0] for i,(x,y) in enumerate(pts))/2
        if abs(area)<1e-10:raise ValueError('Degenerate polygon')
        attrs=self._record(name,meaning,evidence,status,'polygon',[min(x for x,y in pts),min(y for x,y in pts),max(x for x,y in pts),max(y for x,y in pts)])
        self.parts.append('<polygon {} points="{}" fill="{}" stroke="{}" stroke-width="1.5"/>'.format(attrs,' '.join('{},{}'.format(*p) for p in pts),paint(fill),paint(stroke)))
        return self

    def route(self,name,start,end,*,via=(),meaning,evidence,status='schematic',stroke='active',width=2,arrow=True):
        if start not in self.anchors or end not in self.anchors:raise ValueError('A route must use two declared anchors')
        pts=[self.anchors[start]['point']]+[point(p) for p in via]+[self.anchors[end]['point']]
        if any(math.dist(a,b)<1e-9 for a,b in zip(pts,pts[1:])):raise ValueError('Route contains a zero-length segment')
        finite(width,True)
        attrs=self._record(name,meaning,evidence,status,'route',[min(x for x,y in pts),min(y for x,y in pts),max(x for x,y in pts),max(y for x,y in pts)])
        self.marks[name].update(start=start,end=end,points=pts)
        self.parts.append('<polyline {} points="{}" fill="none" stroke="{}" stroke-width="{}" stroke-linejoin="round"/>'.format(attrs,' '.join('{},{}'.format(*p) for p in pts),paint(stroke),width))
        if arrow:
            a,b=pts[-2:];t=math.atan2(b[1]-a[1],b[0]-a[0]);length=4*width;side=1.8*width
            triangle=[b,(b[0]-length*math.cos(t)+side*math.sin(t),b[1]-length*math.sin(t)-side*math.cos(t)),(b[0]-length*math.cos(t)-side*math.sin(t),b[1]-length*math.sin(t)+side*math.cos(t))]
            self.parts.append('<polygon points="{}" fill="{}"/>'.format(' '.join('{},{}'.format(*p) for p in triangle),paint(stroke)))
            xs=[p[0] for p in triangle]+[p[0] for p in pts];ys=[p[1] for p in triangle]+[p[1] for p in pts]
            self.marks[name]['bounds']=[min(xs),min(ys),max(xs),max(ys)]
        return self

    def label(self,name,xy,text,*,for_mark,font_pt=8,anchor='start'):
        if for_mark not in self.marks:raise ValueError('Label must identify an existing scientific mark')
        if not isinstance(text,str) or not text.strip():raise ValueError('Nonempty label required')
        finite(font_pt,True)
        if font_pt<self.min_font:raise ValueError('Label below declared physical-size minimum')
        if anchor not in {'start','middle','end'}:raise ValueError('Unknown text anchor')
        x,y=point(xy);owner=self.marks[for_mark]
        attrs=self._record(name,'Label for '+for_mark,owner['evidence_ids'],owner['status'],'label',[x,y,x,y])
        self.marks[name].update(for_mark=for_mark,font_pt=font_pt)
        font_units=font_pt*25.4/72*self.unit
        self.parts.append('<text {} data-mf-label="{}" x="{}" y="{}" font-family="Arial,Helvetica,sans-serif" font-size="{}" text-anchor="{}" fill="{}">{}</text>'.format(attrs,for_mark,x,y,font_units,anchor,paint('ink'),html.escape(text)))
        return self

    def audit(self):
        failures=[]
        for m in self.marks.values():
            x1,y1,x2,y2=m['bounds']
            if x1<0 or y1<0 or x2>self.width or y2>self.height:failures.append(m['id']+': geometry outside viewBox')
        for name,a in self.anchors.items():
            x,y=a['point'];x1,y1,x2,y2=self.marks[a['owner']]['bounds']
            if not (x1-1e-6<=x<=x2+1e-6 and y1-1e-6<=y<=y2+1e-6):failures.append(name+': anchor outside owner bounds')
        return {'status':'geometry_checks_pass' if not failures else 'needs_revision','errors':failures,
                'not_checked':['scientific correctness','collision/occlusion','text extent or overlap','visual quality'],
                'next':'Inspect the real render at final size and 4x; validate evidence IDs against figure.json.'}

    def svg(self):
        audit=self.audit()
        if audit['errors']:raise ValueError('; '.join(audit['errors']))
        return '<svg xmlns="http://www.w3.org/2000/svg" width="{}mm" height="{}mm" viewBox="0 0 {} {}"><title>{}</title><desc>{}</desc>\n{}\n</svg>\n'.format(self.width_mm,self.height_mm,self.width,self.height,html.escape(self.title),html.escape(self.description),'\n'.join(self.parts))

    def save(self,path):
        path=Path(path)
        if path.suffix.lower()!='.svg':raise ValueError('Write an editable .svg file')
        if path.exists() or path.with_suffix('.scene.json').exists():raise FileExistsError('Refusing to overwrite an existing figure or scene record')
        svg=self.svg();path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(svg,encoding='utf-8')
        manifest={'width_mm':self.width_mm,'height_mm':self.height_mm,'units_per_mm':self.unit,'marks':list(self.marks.values()),'anchors':self.anchors,'audit':self.audit()}
        path.with_suffix('.scene.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
        return manifest
