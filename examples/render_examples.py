#!/usr/bin/env python3
"""Original analytical demonstrations, not reproductions or empirical research results.

Python standard library only. Produces exact-data SVGs; use a browser or vector
renderer to produce the corresponding PNG previews. No image or model service.
"""
from __future__ import annotations
import argparse
import html
import json
import math
from pathlib import Path
import shutil

INK, CONTEXT, ACCENT, CHANGE = '#24332e', '#6b766e', '#315f51', '#ab693b'


def project(x, y):
    return max(0.0, x), y


def state(t):
    """Exact two-filter response: forcing=1 for 0<=t<=2, then 0."""
    def component(tau):
        if t <= 2: return 1 - math.exp(-t / tau)
        return (1 - math.exp(-2 / tau)) * math.exp(-(t - 2) / tau)
    return component(0.2), component(0.8)


def check_math():
    results = {}
    for x, y in [(-1.8, 1.2), (0, 2), (1.4, -0.5), (-3, 0)]:
        px, py = project(x, y)
        assert px >= 0 and py == y
        assert project(px, py) == (px, py)
        for qx in [0, 0.2, 1, 2]:
            for qy in [-1, 0, y, 3]:
                assert (px-x)**2 + (py-y)**2 <= (qx-x)**2 + (qy-y)**2 + 1e-12
    results['projection_feasibility_idempotence_and_sampled_nearest_point_checks'] = True
    rise = 0.8 * math.log(2)
    fall = 2 + 0.8 * math.log((1 - math.exp(-2 / 0.8)) / 0.5)
    assert abs(state(rise)[1] - 0.5) < 1e-12
    assert abs(state(fall)[1] - 0.5) < 1e-12
    assert state(rise)[0] > state(fall)[0]
    for t in [0.1, 0.7, 1.6, 2.3, 3.9]:
        u = 1 if t < 2 else 0
        for j, tau in enumerate([0.2, 0.8]):
            derivative = (state(t+1e-6)[j]-state(t-1e-6)[j])/(2e-6)
            assert abs(derivative-(u-state(t)[j])/tau) < 1e-7
    results['analytic_lag_solution_and_equal_readout_opposite_direction'] = True
    return results


class SVG:
    def __init__(self, title, desc):
        self.parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="180mm" height="105mm" viewBox="0 0 1080 630">', '<title>'+html.escape(title)+'</title><desc>'+html.escape(desc)+'</desc>', '<rect width="1080" height="630" fill="white"/>']
    def text(self, x, y, value, size=19, color=INK, anchor='start'):
        self.parts.append('<text x="{}" y="{}" font-family="Arial,Helvetica,sans-serif" font-size="{}" fill="{}" text-anchor="{}">{}</text>'.format(x,y,size,color,anchor,html.escape(value)))
    def line(self,x1,y1,x2,y2,color=CONTEXT,width=1.5,dash=None):
        self.parts.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" stroke-width="{}"{}/>'.format(x1,y1,x2,y2,color,width,' stroke-dasharray="'+dash+'"' if dash else ''))
    def arrow(self,x1,y1,x2,y2,color=INK,width=3,dash=None):
        self.line(x1,y1,x2,y2,color,width,dash)
        theta=math.atan2(y2-y1,x2-x1);length=11;spread=4.5
        a=(x2-length*math.cos(theta)+spread*math.sin(theta),y2-length*math.sin(theta)-spread*math.cos(theta))
        b=(x2-length*math.cos(theta)-spread*math.sin(theta),y2-length*math.sin(theta)+spread*math.cos(theta))
        self.parts.append('<polygon points="{},{} {},{} {},{}" fill="{}"/>'.format(x2,y2,*a,*b,color))
    def point(self,x,y,color=INK,radius=5): self.parts.append('<circle cx="{}" cy="{}" r="{}" fill="{}"/>'.format(x,y,radius,color))
    def rect(self,x,y,w,h,fill,stroke='none'):
        self.parts.append('<rect x="{}" y="{}" width="{}" height="{}" fill="{}" stroke="{}"/>'.format(x,y,w,h,fill,stroke))
    def path(self,coords,color,width=3):
        self.parts.append('<path d="'+ ' '.join(('M' if i==0 else 'L')+'{:.3f},{:.3f}'.format(x,y) for i,(x,y) in enumerate(coords))+'" fill="none" stroke="'+color+'" stroke-width="'+str(width)+'"/>')
    def save(self,path): path.write_text('\n'.join(self.parts+['</svg>'])+'\n')


def projection(out):
    s=SVG('Projection removes only the forbidden component','Analytical example: the Euclidean projection of (-1.8,1.2) onto x >= 0 is (0,1.2). The tangential coordinate remains unchanged.')
    s.text(48,54,'Remove the forbidden component.',30)
    s.text(48,88,'Analytical demonstration · Euclidean projection onto the halfspace x ≥ 0',18,CONTEXT)
    ox,oy,scale=380,459,125
    x,y=-1.8,1.2; px,py=project(x,y)
    input_point=(ox+scale*x,oy-scale*y); target=(ox+scale*px,oy-scale*py)
    s.rect(ox,140,287,367,'#edf3ef')
    s.line(ox,140,ox,520,ACCENT,2)
    s.arrow(90,oy,671,oy,CONTEXT,1.3)
    s.arrow(ox,520,ox,136,CONTEXT,1.3)
    s.text(662,492,'x',19,CONTEXT);s.text(354,151,'y',19,CONTEXT)
    s.text(408,166,'feasible: x ≥ 0',19,ACCENT)
    s.arrow(ox,oy,*input_point,CONTEXT,3,'8 5')
    s.arrow(ox,oy,*target,ACCENT,5)
    s.arrow(*input_point,*target,CHANGE,3)
    s.point(*input_point,CONTEXT);s.point(*target,ACCENT);s.point(ox,oy,INK,4)
    s.text(80,264,'proposed (−1.8, 1.2)',19)
    s.text(407,303,'projected (0, 1.2)',19,ACCENT)
    s.text(198,293,'normal correction',17,CHANGE)
    s.line(target[0],target[1]+15,target[0]-15,target[1]+15,CONTEXT,1.2)
    s.line(target[0]-15,target[1]+15,target[0]-15,target[1],CONTEXT,1.2)
    s.text(367,487,'0',17,CONTEXT)
    s.line(700,145,700,525,'#d7e1da',1)
    s.text(742,179,'The operation',20)
    s.text(742,217,'P(x, y) = (max(x, 0), y)',20,ACCENT)
    s.text(742,280,'Changes',18,CHANGE)
    s.text(742,311,'normal coordinate: −1.8 → 0',17)
    s.text(742,366,'Preserves',18,ACCENT)
    s.text(742,397,'tangent coordinate: 1.2 → 1.2',17)
    s.text(742,461,'Already feasible?',18)
    s.text(742,492,'The vector does not move.',17,CONTEXT)
    s.line(48,556,1032,556,'#d7e1da',1)
    s.text(48,589,'The nearest feasible point is reached by an orthogonal displacement—not by shrinking the whole vector.',17)
    s.save(out/'figure.svg')
    (out/'data.json').write_text(json.dumps({'kind':'analytical demonstration','input':[x,y],'projection':[px,py],'metric':'Euclidean','constraint':'x >= 0','checks':check_math()},indent=2)+'\n')
    (out/'caption.md').write_text('Euclidean projection onto the halfspace x ≥ 0. The dashed input vector (−1.8, 1.2) is mapped to (0, 1.2); the horizontal displacement removes the infeasible normal component and preserves the tangential coordinate. Equal axis scales are used, and all coordinates are dimensionless. This is an exact analytical toy example, not a measured optimization trajectory, a new algorithm, or a claim about convergence or runtime. Data and checks are generated by render.py.\n')


def lag(out):
    s=SVG('A single readout hides the direction','Two first-order filters respond to the same step input. Their joint state disambiguates rising and falling phases at the same slow readout of 0.5.')
    s.text(48,54,'One readout. Two different futures.',30)
    s.text(48,88,'Analytical demonstration · the same forcing drives a fast and a slow first-order response',18,CONTEXT)
    ox,oy,scale=112,501,346
    at=lambda t:(ox+scale*state(t)[1],oy-scale*state(t)[0])
    s.arrow(ox,oy,507,oy,CONTEXT,1.3);s.arrow(ox,oy,ox,126,CONTEXT,1.3)
    s.text(301,553,'slow response y',19,CONTEXT,anchor='middle')
    s.text(48,129,'fast x',18,CONTEXT)
    for val in [0,.5,1]:
        s.text(ox+scale*val,526,str(val),17,CONTEXT,anchor='middle')
        s.text(95,oy-scale*val+6,str(val),17,CONTEXT,anchor='end')
    times=[i*2/180 for i in range(181)]
    s.path([at(t) for t in times],ACCENT,4)
    s.path([at(2+i*4/280) for i in range(281)],CHANGE,4)
    for t in [.28,.9,1.5]:s.arrow(*at(t),*at(t+.06),ACCENT,3)
    for t in [2.12,2.5,3.1]:s.arrow(*at(t),*at(t+.05),CHANGE,3)
    rise=.8*math.log(2);fall=2+.8*math.log((1-math.exp(-2/.8))/.5)
    a,b=at(rise),at(fall)
    s.line(a[0],140,a[0],oy,CONTEXT,1.4,'4 5')
    s.point(*a,ACCENT,6);s.point(*b,CHANGE,6)
    s.text(a[0]+15,a[1]-36,'A · rising',18,ACCENT)
    s.text(b[0]+15,b[1]+28,'B · falling',18,CHANGE)
    s.text(481,236,'forcing on',17,ACCENT)
    s.text(437,435,'forcing off',17,CHANGE)
    s.line(616,142,616,526,'#d7e1da',1)
    s.text(656,175,'Same slow readout: y = 0.5',21)
    s.text(656,214,'A: fast state x = {:.3f}'.format(state(rise)[0]),18,ACCENT)
    s.text(656,245,'B: fast state x = {:.3f}'.format(state(fall)[0]),18,CHANGE)
    s.text(656,299,'Direction is not in y alone.',20)
    s.text(656,337,'Rising: dy/dt = +0.625',18,ACCENT)
    s.text(656,368,'Falling: dy/dt = −0.625',18,CHANGE)
    s.text(656,423,'dx/dt = (u − x) / 0.2',18)
    s.text(656,452,'dy/dt = (u − y) / 0.8',18)
    s.text(656,494,'u = 1 until t = 2; then u = 0.',17,CONTEXT)
    s.line(48,575,1032,575,'#d7e1da',1)
    s.text(48,606,'Coordinates and arrows come from the specified dynamics. Curvature alone would not establish a time direction.',17)
    s.save(out/'figure.svg')
    data={'kind':'analytic ODE solution sampled for display','tau_fast':.2,'tau_slow':.8,'forcing_switch':2,'equal_readout_states':[{'t':rise,'x':state(rise)[0],'y':state(rise)[1],'dy_dt':.625},{'t':fall,'x':state(fall)[0],'y':state(fall)[1],'dy_dt':-.625}],'trajectory':[{'t':i*.02,'x':state(i*.02)[0],'y':state(i*.02)[1]} for i in range(301)],'checks':check_math()}
    (out/'data.json').write_text(json.dumps(data,indent=2)+'\n')
    (out/'caption.md').write_text('Exact phase-plane trajectory of two first-order filters with time constants 0.2 and 0.8 and shared forcing u(t)=1 for 0≤t≤2, then 0. The initial states are zero. Green denotes forcing on; orange denotes forcing off. At slow response y=0.5 the rising and falling states have different fast response x and derivatives +0.625 and −0.625. States are dimensionless, time uses arbitrary consistent units, and arrows follow increasing time. This analytical illustration is not a reconstruction from biological snapshots and does not claim that arbitrary curved embeddings identify dynamics.\n')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kind',choices=['projection','lag','all'],default='all')
    parser.add_argument('--output',type=Path,default=Path(__file__).parent/'generated')
    args=parser.parse_args()
    kinds=['projection','lag'] if args.kind=='all' else [args.kind]
    for kind in kinds:
        out=args.output/kind if args.kind=='all' else args.output
        out.mkdir(parents=True,exist_ok=True)
        globals()[kind](out)
        source=Path(__file__).resolve(); dest=(out/'render.py').resolve()
        if source!=dest:shutil.copyfile(source,dest)
        print(json.dumps({'example':kind,'output':str(out),'checks':check_math(),'status':'vector_generated; PNG and visual review still required'}))


if __name__=='__main__':main()
