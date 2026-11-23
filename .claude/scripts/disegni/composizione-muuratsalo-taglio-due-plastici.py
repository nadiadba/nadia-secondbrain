"""Taglio dei due plastici di Muuratsalo (pezzi M e N) sullo stesso foglio 70 x 50: MaxRects,
pezzi stretti in alto a sinistra. Legge pezzi.json (plastico di Aalto) e pezzi-n.json (secondo plastico)."""
import json, sys
M = json.load(open("pezzi.json")); N = json.load(open("pezzi-n.json"))
W, H, GAP = 70.0, 50.0, 0.0
def norm(p):
    xs=[q[0] for q in p["outline"]]; ys=[q[1] for q in p["outline"]]
    x0,y0=min(xs),min(ys)
    f=lambda pts:[[q[0]-x0,q[1]-y0] for q in pts]
    return dict(cod=p["cod"],nome=p["nome"],outline=f(p["outline"]),holes=[f(h) for h in p["holes"]],w=max(xs)-x0,h=max(ys)-y0)
def ruota(p):  # 90 gradi: (x,y) -> (h-y, x)
    g=lambda pts:[[p["h"]-y,x] for x,y in pts]
    return dict(p,outline=g(p["outline"]),holes=[g(h) for h in p["holes"]],w=p["h"],h=p["w"])
P=[norm(p) for p in M+N]
P=[ruota(p) if p["h"]>p["w"] else p for p in P]
E=1e-9
def pack(items, W, H, ordine):
    free=[(0,0,W,H)]; placed=[]
    for p in ordine(items):
        best=None
        for rot in (0,1):
            w,h=(p["w"],p["h"]) if not rot else (p["h"],p["w"])
            for fx,fy,fw,fh in free:
                if w<=fw+E and h<=fh+E:
                    # in alto a sinistra; a parita', accanto a un pezzo della stessa altezza
                    vic=any(abs(q[1]-fy)<E and abs(q[3]-h)<0.06 and abs(q[0]+q[2]-fx)<E for q in placed)
                    key=(round(fy+h,3)*0+round(fy,3), 0 if vic else 1, round(fx,3), rot)
                    if best is None or key<best[0]: best=(key,fx,fy,w,h,rot)
        if best is None: return None
        _,x,y,w,h,rot=best
        placed.append((x,y,w,h,p,rot))
        nf=[]
        for fx,fy,fw,fh in free:
            if x>=fx+fw-E or x+w<=fx+E or y>=fy+fh-E or y+h<=fy+E: nf.append((fx,fy,fw,fh)); continue
            if x>fx+E: nf.append((fx,fy,x-fx,fh))
            if x+w<fx+fw-E: nf.append((x+w,fy,fx+fw-x-w,fh))
            if y>fy+E: nf.append((fx,fy,fw,y-fy))
            if y+h<fy+fh-E: nf.append((fx,y+h,fw,fy+fh-y-h))
        free=[a for a in nf if not any(b!=a and b[0]<=a[0]+E and b[1]<=a[1]+E and b[0]+b[2]>=a[0]+a[2]-E and b[1]+b[3]>=a[1]+a[3]-E for b in nf)]
        free=list(dict.fromkeys(free))
    return placed
ordini={
 "altezza": lambda it: sorted(it,key=lambda p:(-round(p["h"],1),-p["w"])),
 "area": lambda it: sorted(it,key=lambda p:(-p["w"]*p["h"])),
 "lato": lambda it: sorted(it,key=lambda p:(-max(p["w"],p["h"]),-min(p["w"],p["h"]))),
}
best=None
for nome,o in ordini.items():
    for Wt in [70]:
        for H in [x/4 for x in range(100,201)]:
            r=pack(P,Wt,H,o)
            if r:
                used_h=max(y+h for x,y,w,h,p,rot in r); used_w=max(x+w for x,y,w,h,p,rot in r)
                print(nome,H,round(used_h,2),round(used_w,2))
                if best is None or used_h<best[0]: best=(used_h,nome,r)
                break
used_h,nome,r=best
print("scelto",nome,used_h)
def ruota(p):
    g=lambda pts:[[p["h"]-y,x] for x,y in pts]
    return dict(p,outline=g(p["outline"]),holes=[g(h) for h in p["holes"]],w=p["h"],h=p["w"])
DATI=[]
for x,y,w,h,p,rot in r:
    q=ruota(p) if rot else p
    sh=lambda pts:[[round(a+x,3),round(b+y,3)] for a,b in pts]
    DATI.append({"cod":q["cod"],"nome":q["nome"],"outline":sh(q["outline"]),"holes":[sh(hh) for hh in q["holes"]]})
json.dump(DATI,open("dati-due-plastici.json","w"))
