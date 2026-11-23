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
# altezze arrotondate al mm per raggruppare
P.sort(key=lambda p:(-round(p["h"],1), -p["w"]))
shelves=[]  # [y, h, x_libero, pezzi]
y=0
for p in P:
    for s in shelves:
        if s[2]+p["w"]<=W+1e-9 and p["h"]<=s[1]+1e-9:
            p["x"],p["y"]=s[2],s[0]; s[2]+=p["w"]+GAP; s[3].append(p); break
    else:
        s=[y,p["h"],p["w"]+GAP,[p]]; p["x"],p["y"]=0,y; shelves.append(s); y+=p["h"]+GAP
print("altezza usata",round(y,2), "ripiani",len(shelves))
for s in shelves: print(round(s[0],2), round(s[1],2), round(s[2],2), [q["cod"] for q in s[3]])
DATI=[]
for p in P:
    sh=lambda pts:[[round(x+p["x"],3),round(y+p["y"],3)] for x,y in pts]
    DATI.append({"cod":p["cod"],"nome":p["nome"],"outline":sh(p["outline"]),"holes":[sh(h) for h in p["holes"]]})
T=open("template.html").read()
def R(a,b):
    global T
    assert T.count(a)==1,a[:50]; T=T.replace(a,b)
R("<title>Taglio del Poliplat</title>","<title>Taglio dei due plastici</title>")
R("<h1>Taglio del Poliplat · casa di Muuratsalo</h1>","<h1>Taglio del Poliplat · i due plastici di Muuratsalo</h1>")
R("Trascina i pezzi rosa sul foglio verde 70 × 50 cm.","Sullo stesso foglio verde 70 × 50 cm ci sono i pezzi del plastico della casa di Aalto (rosa, codici M) e quelli del tuo progetto (azzurri, codici N), mescolati: i pezzi della stessa altezza stanno nella stessa fila, così si tagliano con una sola linea lunga. Trascinali dove vuoi.")
R('.pezzo.bad path.forma {','.pezzo.n path.forma { fill: #c4dcf2; stroke: #2f5f8f; }\n.pezzo.bad path.forma {')
R('const DATI = __DATI__;','const DATI = '+json.dumps(DATI)+';')
R('CHIAVE = "muuratsalo-taglio-v1"','CHIAVE = "muuratsalo-taglio-due-plastici-v1"')
R('  g.dataset.i = i;','  g.dataset.i = i; if (p.cod.startsWith("N")) g.classList.add("n");')
R('aria-label="Foglio di Poliplat 70 per 50 centimetri con i pezzi del plastico"','aria-label="Foglio di Poliplat 70 per 50 centimetri con i pezzi dei due plastici"')
open("taglio-due-plastici.html","w").write(T)
json.dump(DATI,open("dati-due-plastici.json","w"))
