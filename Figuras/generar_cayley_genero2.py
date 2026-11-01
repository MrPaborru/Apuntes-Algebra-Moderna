"""Regenera CayleyGeneroDos.tex; no se necesita Python para compilar los apuntes.

Teselacion {8,8} del disco de Poincare. El octagono tiene angulos pi/4;
se identifican los lados segun la palabra a b a^-1 b^-1 c d c^-1 d^-1.
La presentacion resultante es <a,b,c,d | [a,b][c,d]>.
Su cociente tiene una cara, cuatro aristas y un vertice: genero 2.
El trazado combina radios circulares mayores con una deformacion radial
simetrica que da mas recorrido interior. No representa geodesicas exactas.
"""
from pathlib import Path
import cmath
import math

NIVELES = 6
LONGITUD_MINIMA = .001
ESCALA_CM = 4.25
FACTOR_RADIO_ARCOS = 1.8
RECORRIDO_INTERIOR = 1.6  # 1.0 conserva las posiciones originales.
# Ambos parametros en 1.0 recuperan las geodesicas de Poincare.
RADIO_VERTICE = math.sqrt(math.cos(math.pi / 4))
vertices = [RADIO_VERTICE * cmath.exp(1j * math.pi * k / 4) for k in range(8)]
# Vista original, centrada en la cara octagonal, sin rotacion ni traslacion.
def vista(z):
    return z

def deformar(z):
    return z*abs(z)**(RECORRIDO_INTERIOR-1)

def derivada_deformacion(z,v):
    r=abs(z)
    if r<1e-12:
        return 0j
    return r**(RECORRIDO_INTERIOR-1)*(v+(RECORRIDO_INTERIOR-1)*z*(z.conjugate()*v).real/r**2)
# Circulo ortogonal al borde que contiene el primer lado.
centro_lado = (1 + RADIO_VERTICE**2) / (2 * RADIO_VERTICE * math.cos(math.pi / 8))
apotema = centro_lado - math.sqrt(centro_lado**2 - 1)
traslacion = 2 * apotema / (1 + apotema**2)
A = 1 / math.sqrt(1 - traslacion**2)
pareja = [2, 3, 0, 1, 6, 7, 4, 5]
generadores = []
for k in range(8):
    # Rota el lado emparejado hasta el opuesto y traslada sobre la normal.
    giro = (k-pareja[k])*math.pi/4 + math.pi
    fase = cmath.exp(1j*giro/2)
    t = traslacion * cmath.exp(1j*(k+.5)*math.pi/4)
    generadores.append((A*fase, A*t*fase.conjugate()))

def transformar(a, b, z):
    return (a * z + b) / (b.conjugate() * z + a.conjugate())

def clave(z):
    return (round(z.real, 8), round(z.imag, 8))

aristas = {}
etiquetas = {}
vistos = set()
pendientes = [(1+0j, 0j, -1, 0)]
for a, b, anterior, nivel in pendientes:
    centro = transformar(a, b, 0j)
    if clave(centro) in vistos:
        continue
    vistos.add(clave(centro))
    poligono = [vista(transformar(a, b, z)) for z in vertices]
    for k, u in enumerate(poligono):
        v = poligono[(k+1) % 8]
        if abs(u-v) > LONGITUD_MINIMA:
            llave = tuple(sorted((clave(u), clave(v))))
            if llave not in aristas:
                aristas[llave] = (u, v)
                etiquetas[llave] = ['a','b','a^{-1}','b^{-1}','c','d','c^{-1}','d^{-1}'][k]
    if nivel < NIVELES:
        for k, (c, d) in enumerate(generadores):
            if anterior >= 0 and k == pareja[anterior]:
                continue
            pendientes.append((a*c + b*d.conjugate(), a*d+b*c.conjugate(), k, nivel+1))

# Los vertices del octagono fundamental deben tener exactamente ocho vecinos.
for z in map(vista,vertices):
    assert sum(clave(z) in e for e in aristas) == 8

lineas = [
    '% Generado por generar_cayley_genero2.py: teselacion hiperbólica {8,8}.',
    '% Radios circulares mayores y deformacion radial simetrica del interior.',
    '% Identificacion de lados: a b a^{-1} b^{-1} c d c^{-1} d^{-1}.',
    '% Centrado original; curvas Bezier sin rotacion ni cambio del circulo exterior.',
    rf'\begin{{tikzpicture}}[x={ESCALA_CM}cm,y={ESCALA_CM}cm,line cap=round,line join=round]',
    r'\path[use as bounding box] (-1.015,-1.015) rectangle (1.015,1.015);',
    r'\begin{scope}',
    r'\clip (0,0) circle[radius=1];',
]
geodesicas = {}
trazos = {}
def camino_bezier(u,v,c,radio,inicio,giro):
    # Aproximacion adaptativa de la curva deformada: error menor que .001 pt.
    def evaluar(t):
        z=c+radio*cmath.exp(1j*math.radians(inicio+t*giro))
        dz=1j*math.radians(giro)*(z-c)
        return deformar(z),derivada_deformacion(z,dz)
    def trozo(t0,t1,profundidad=0):
        p0,d0=evaluar(t0);p3,d3=evaluar(t1);dt=t1-t0
        p1=p0+d0*dt/3;p2=p3-d3*dt/3
        error=0
        for t in (.25,.5,.75):
            b=(1-t)**3*p0+3*(1-t)**2*t*p1+3*(1-t)*t*t*p2+t**3*p3
            error=max(error,abs(b-evaluar(t0+t*dt)[0]))
        if error>5e-6 and profundidad<9:
            m=(t0+t1)/2
            return trozo(t0,m,profundidad+1)+trozo(m,t1,profundidad+1)
        return [(p0,p1,p2,p3)]
    partes=trozo(0,1)
    # Los extremos se comparten exactamente con las aristas adyacentes.
    partes[0]=(deformar(u),*partes[0][1:])
    partes[-1]=(*partes[-1][:3],deformar(v))
    return partes

for llave, (u, v) in aristas.items():
    # Resuelve Re(conj(u)*c)=(1+|u|^2)/2 para el centro c del arco.
    det = u.real*v.imag - u.imag*v.real
    grosor = '.5' if abs(u-v)>.1 else '.22'
    if abs(det) < 1e-8:
        lineas.append(r'\draw[line width=%spt] (%.9f,%.9f)--(%.9f,%.9f);' % (grosor,u.real,u.imag,v.real,v.imag))
        continue
    ru, rv = (1+abs(u)**2)/2, (1+abs(v)**2)/2
    c = complex((ru*v.imag-rv*u.imag)/det, (u.real*rv-v.real*ru)/det)
    radio = abs(u-c)*FACTOR_RADIO_ARCOS
    medio = (u+v)/2
    normal = (c-medio)/abs(c-medio)
    c = medio+normal*math.sqrt(radio**2-abs(u-v)**2/4)
    inicio = math.degrees(cmath.phase(u-c))
    fin = math.degrees(cmath.phase(v-c))
    giro = (fin-inicio+180) % 360-180
    geodesicas[llave] = (c, radio, inicio, giro)
    partes=camino_bezier(u,v,c,radio,inicio,giro)
    trazos[llave]=partes
    p=partes[0][0]
    comando=r'\draw[line width=%spt] (%.9f,%.9f)' % (grosor,p.real,p.imag)
    for _,p1,p2,p3 in partes:
        comando+=r' .. controls (%.9f,%.9f) and (%.9f,%.9f) .. (%.9f,%.9f)' % (p1.real,p1.imag,p2.real,p2.imag,p3.real,p3.imag)
    lineas.append(comando+';')
lineas += [r'\end{scope}', r'\draw[line width=.3pt] (0,0) circle[radius=1];']
# Se conservan solo las etiquetas principales; %% permite reactivarlas en LaTeX.
lineas.append('%% Etiquetas principales: quitar %% de los nodos para mostrarlas.')
for k in range(8):
    z = deformar(vista((apotema-.09)*cmath.exp(1j*(k+.5)*math.pi/4)))
    etiqueta = ['a','b','a^{-1}','b^{-1}','c','d','c^{-1}','d^{-1}'][k]
    lineas.append(r'%%%% \node[font=\fontsize{8}{9}\selectfont,inner sep=0pt] at (%.7f,%.7f) {$%s$};' % (z.real,z.imag,etiqueta))
lineas += [r'\end{tikzpicture}', '']
Path(__file__).with_name('CayleyGeneroDos.tex').write_text('\n'.join(lineas),encoding='utf-8')
print(f'{len(vistos)} octagonos; {len(aristas)} aristas; etiquetas principales comentadas; valencia central 8 comprobada.')
