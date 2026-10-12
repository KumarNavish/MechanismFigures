"""Explicit geometry, with no inferred physical interpretation or hidden perspective."""
import math


def point(value, dimensions=2):
    if len(value) != dimensions or any(type(x) not in (int, float) or not math.isfinite(x) for x in value):
        raise ValueError('Expected a finite {}D point'.format(dimensions))
    return tuple(float(x) for x in value)


def project(points, azimuth=45.0, elevation=30.0):
    """Orthographic camera: x/y on the floor, z up; returns (screen_x, screen_y, depth).

    This transforms declared world coordinates, not latent distances into physical ones.
    Positive depth is toward the viewer. Occlusion still needs a proper scene renderer.
    """
    if not all(type(x) in (int, float) and math.isfinite(x) for x in [azimuth, elevation]):
        raise ValueError('Camera angles must be finite degrees')
    a, e = math.radians(azimuth), math.radians(elevation)
    result = []
    for xyz in points:
        x, y, z = point(xyz, 3)
        right = -math.sin(a)*x + math.cos(a)*y
        up = -math.sin(e)*math.cos(a)*x - math.sin(e)*math.sin(a)*y + math.cos(e)*z
        depth = math.cos(e)*math.cos(a)*x + math.cos(e)*math.sin(a)*y + math.sin(e)*z
        result.append((right, -up, depth))
    return result


def fit(points, width, height, padding=20):
    """Uniform scale and translation; never independently stretch axes to fill a frame."""
    pts = [point(p) for p in points]
    if not pts or not all(type(x) in (int, float) and math.isfinite(x) for x in [width,height,padding]):
        raise ValueError('Finite nonempty geometry and dimensions are required')
    if padding < 0 or min(width,height) <= 2*padding:
        raise ValueError('Padding leaves no drawable region')
    lo = [min(p[d] for p in pts) for d in (0,1)]
    hi = [max(p[d] for p in pts) for d in (0,1)]
    span = [hi[d]-lo[d] for d in (0,1)]
    scales = [(width-2*padding)/span[0] if span[0] else math.inf,
              (height-2*padding)/span[1] if span[1] else math.inf]
    scale = min(scales)
    if not math.isfinite(scale): scale = 1.0
    offset = [width/2-scale*(lo[0]+hi[0])/2, height/2-scale*(lo[1]+hi[1])/2]
    return {'points': [(x*scale+offset[0],y*scale+offset[1]) for x,y in pts],
            'scale': scale, 'offset': offset, 'input_bounds': [*lo,*hi]}


def transform(points, matrix=(1,0,0,1,0,0)):
    """Apply an explicit SVG affine transform; callers own the scientific meaning."""
    if len(matrix)!=6 or any(type(x) not in (int,float) or not math.isfinite(x) for x in matrix):
        raise ValueError('Expected six finite affine coefficients')
    a,b,c,d,e,f=matrix
    return [(a*x+c*y+e,b*x+d*y+f) for x,y in map(point,points)]
