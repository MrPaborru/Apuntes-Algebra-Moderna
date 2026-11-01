# Formato y notación

## Composición del documento

El texto utiliza NewTX a 12 puntos, papel carta y márgenes de una pulgada. La matemática principal se compone con NewTX, opción `libertine`; `\mathbb` utiliza la familia `lmsb` de **LXfonts** y `\mathcal`, la caligráfica Euler de **eucal**.

Los cinco capítulos numerados corresponden a preliminares, grupos, anillos, módulos y campos con teoría de Galois. El índice fluye continuamente y destaca cada capítulo con su número en un recuadro claro y su título centrado en una franja burdeos. Los encabezados indican el capítulo. Teoremas, proposiciones, lemas y corolarios comparten un contador por capítulo; las definiciones y los ejemplos se numeran por sección. Los ejercicios tienen su propio contador por capítulo, recuadro burdeos y solución inmediata. Las observaciones no llevan número. La bibliografía utiliza natbib y BibTeX, con estilo `plainnat`.

La portada incluye el título, el periodo del curso, su clave, el grafo de Cayley dibujado en TikZ, el docente y el autor. El índice tiene su título centrado y franjas de capítulo sin folio. En el texto, los números de sección son burdeos; los títulos de subsección son grises, con el número blanco sobre un recuadro gris. Los separadores admiten títulos largos en varias líneas y conservan el escudo, la paleta y el banner. El pie de portada contiene la fecha de compilación y el correo enlazado.

Las aperturas de capítulo incluyen sus secciones numeradas en dos columnas abiertas bajo el título, a todo el ancho del texto, sin folios y con enlaces al texto. El título se alinea a la izquierda y encabeza el miniíndice; una línea fina separa ambos. Los números burdeos y el texto gris conservan la paleta institucional. `IndiceCapitulo.tex` obtiene estas entradas automáticamente del índice general; `latexmk` mantiene actualizada la lista. El marcador del capítulo se eleva 1 cm y queda separado del bloque formado por el título y las secciones. El diseño original está respaldado en `Respaldos/Titulos-2026-10-31/`, junto con una muestra PDF de las cinco aperturas.

## Paleta y diagramas

| Nombre | Color | Uso |
| --- | --- | --- |
| `rojoCIMAT` | `#6F263D` | Recuadros, portada y cierre de pruebas |
| `grisCIMAT` | `#888B8D` | Índice, separadores y rellenos claros |
| `rojoDiagramaCIMAT` | `#8A1E43` | Mediadores, recorridos y relaciones destacadas |
| negro | `#000000` | Flechas, contornos y etiquetas ordinarias |
| `azulAlgebra` | `#244A73` | Sectores geométricos |
| `verdeAlgebra` | `#376B63` | Sectores geométricos |
| `ocreAlgebra` | `#9A6B25` | Sectores geométricos |

Las flechas son **negras por defecto**. El estilo `estructura` usa negro; `destacado` usa `rojoDiagramaCIMAT`. El énfasis señala una relación matemática concreta y se acompaña de etiquetas o trazos que permiten reconocerla también sin color.

Azul, verde y ocre son colores auxiliares para distinguir los sectores del hexágono. Los ejes y el recorrido del árbol usan rojo, las demás aristas son negras y los triángulos tienen relleno gris claro. Los rótulos se separan de los trazos para mantener legibles bases y exponentes.

Las ilustraciones independientes se insertan con `\figuraApuntes{Figuras/archivo}{fig:etiqueta}{Título breve}`, definido en `Figuras.tex`. Pueden colocarse aquí o en los extremos de una página cercana para que el texto aproveche el espacio disponible. Los pies numerados y las referencias en el texto permiten identificarlas. Las aperturas de capítulo vacían las figuras pendientes; las secciones permiten continuar el texto, para no forzar páginas incompletas cuando una ilustración acaba de pasar a la siguiente. Los diagramas integrados en las demostraciones permanecen en su posición matemática y conservan su tamaño. Las reservas de espacio antes de ejercicios se limitan a seis líneas para evitar huecos innecesarios.

La identidad gráfica toma como referencia el [Manual Básico de Imagen del CIMAT](https://www.cimat.mx/wp-content/uploads/2022/09/Manual-ba%CC%81sico-de-logotipo.pdf). La definición de los colores utilizados está en `Paleta.tex`.

## Comandos matemáticos

`Simbolos.tex` reúne operadores, categorías y delimitadores. Los operadores estándar, como `\hom`, `\Re`, `\Im` y `\ker`, conservan su significado. La declaración del alfabeto personalizado es `\DeclareMathAlphabet{\mathbb}{U}{lmsb}{m}{n}`; utiliza la fuente `lmsbm8` de LXfonts.

| Comandos | Uso |
| --- | --- |
| `\set`, `\given`, `\SetSymbol` | Conjuntos por comprensión y barra separadora ajustable |
| `\ang`, `\generado` | Delimitadores angulares con `\given`; `\generado` es un alias de `\ang` |
| `\brack`, `\Brack`, `\floor`, `\ceil`, `\round` | Corchetes, piso, techo y delimitadores mixtos |
| `\restr`, `\supsub`, `\ubar` | Restricción, índices pequeños y barra superior |
| `\en`, `\noten`, `\cont`, `\dotcup` | Pertenencia, no pertenencia, pertenencia inversa y unión disjunta |
| `\bigforall`, `\bigexists`, `\colonequiv` | Cuantificadores ampliados y equivalencia por definición |
| `\Hom`, `\Aut`, `\aut`, `\End`, `\Sym`, `\gal`, `\rk`, `\card`, `\coker` | Operadores algebraicos |
| `\im`, `\mcd`, `\mcm`, `\dom`, `\cod`, `\id`, `\ord`, `\res`, `\supp`, `\ev` | Operadores de funciones y estructuras algebraicas |
| `\Stab` | Estabilizadores |
| `\Ob`, `\ob`, `\Set`, `\Grp`, `\Ab`, `\Vect`, `\cat`, `\Col` | Objetos, categorías y colecciones |

Los delimitadores admiten tamaño normal, automático con `*` y explícito con `[...]`:

```latex
\set{x \in G \given x^2=e}
\set*{\frac{a}{b} \given a\in\mathbb Z,\ b\ne0}
\set[\Big]{x\in R \given x\ne0}
\ang{x,y \given x^2=y^3=e}
\floor*{\frac{n}{2}}
\restr{f}{H}
```

La definición de `\given` es local a cada uso de `\set` y `\ang`, incluso al anidarlos. `\restr` ajusta la altura de su barra. `\ubar` representa una **barra superior**. `\aut` y `\ob` son alias de `\Aut` y `\Ob`.

Los subgrupos y submódulos generados se escriben con `\ang{A}`; si los generadores llevan una condición, se utiliza `\ang{a_i\given i\in I}`. Las imágenes de elementos bajo una aplicación se indican con `\mapsto`, también en los recorridos de permutaciones.

`\brack{...}` representa corchetes simples. Para una fracción sin barra con corchetes puede utilizarse `\genfrac{[}{]}{0pt}{}{n}{k}`.

`Referencias.tex` define `\myref{etiqueta}` (tipo, número y nombre, si existe) y `\abvref{etiqueta}` (tipo abreviado y número). Los contadores alias permiten que las referencias distingan teoremas, proposiciones, lemas y corolarios. El entorno `sol` admite un título opcional, como `\begin{sol}[Otra solución]`.

## Convenciones matemáticas

Las permutaciones se componen como funciones: el factor derecho actúa primero. El grupo diédrico `D_{2n}` tiene orden `2n`. Para un subgrupo arbitrario, `G/H` es un conjunto de clases izquierdas; sólo es grupo cociente si `H` es normal. Se usan `Z(G)` para el centro, `Z_G(a)` para el centralizador y `N_G(H)` para el normalizador.

El conmutador `G'` es el subgrupo generado por los conmutadores `ghg^{-1}h^{-1}`. `G^{(i)}` denota la serie derivada. Característico significa invariante bajo automorfismos; plenamente invariante, bajo endomorfismos. En un producto semidirecto, `(n,h)(m,k)=(n\theta_h(m),hk)`.

Los anillos tienen unidad y los homomorfismos la preservan; se admite el anillo cero. La conmutatividad se exige cuando se indica. Dominios y campos son no nulos. Bajo la convención de unidades laterales utilizada, `uv=1` hace de `u` una unidad por la izquierda y de `v` su inverso por la derecha. La definición de anillo de división admite el anillo cero; la de campo lo excluye.

Los ideales son bilaterales salvo precisión. Los subanillos contienen la unidad del anillo ambiente. La característica puede ser cero y se toma `\deg0=-\infty`. Dividir por un polinomio mónico no exige que los coeficientes formen un campo.

Los módulos son izquierdos y unitarios. `R^{\oplus A}` es el módulo de funciones de soporte finito y `\ang{A}` es el submódulo generado. Los generadores canónicos de un módulo libre son distintos cuando `R\ne0`. La suma puntual hace de `\Hom_R(M,N)` un grupo abeliano; la estructura por escalares puntuales requiere `R` conmutativo.

Una `R`-álgebra incluye un homomorfismo estructural de imagen central y su anillo puede ser no conmutativo. El álgebra de polinomios `R[A]` es libre en la categoría de álgebras **conmutativas**. «Finita» significa finitamente generada como módulo y «de tipo finito», como álgebra.

En un dominio, «primo» significa que el ideal principal es primo, de modo que puede incluir a cero. Para comparar con irreducibles se exige «primo no nulo». DFU significa dominio de factorización única; los factores se comparan salvo asociados y orden. El mcd también se determina salvo asociados.

`K(R)` es el campo de fracciones y `R(x)=K(R[x])` el campo de funciones racionales formales. Para el contenido de un polinomio no nulo se usa `\operatorname{cont}(f)`, abreviado `c_f`, y `C_f=(c_f)` para su ideal. `\cont` sigue significando pertenencia inversa.

El rango de un módulo libre sobre un dominio es la cardinalidad de un independiente maximal; en módulos finitamente generados se usa el máximo tamaño de una familia independiente. Se escriben `\operatorname{Tor}_R(M)` y `\operatorname{Ann}_R(M)` para torsión y anulador. Las capas `q^{\ell-1}T_q/q^\ell T_q` son espacios vectoriales sobre `R/(q)`.

`[F:k]` es el grado de una extensión como dimensión. `k(\alpha)` es el subcampo generado por `k` y `\alpha` en una extensión fijada; en el caso simple finito se presenta como `k[t]/(p)`, con `p` el polinomio mínimo mónico. `\Aut_k(F)` fija `k` punto por punto.

`k(\alpha_1,\ldots,\alpha_r)` denota generación como campo, que permite divisiones; se distingue de la generación como álgebra `k[\alpha_1,\ldots,\alpha_r]` y de la dimensión finita sobre `k`. Una clausura algebraica `\overline k/k` es algebraica y tiene campo superior algebraicamente cerrado. Se habla de campo de descomposición y separabilidad de polinomios no nulos; sus raíces se cuentan con multiplicidades. La normalidad exige descomposición completa de cada irreducible con alguna raíz en la extensión. En característica prima, `\operatorname{Frob}_k(a)=a^p`. Un campo perfecto tiene característica cero o Frobenius sobreyectivo. La separabilidad de extensiones se considera para extensiones algebraicas; `[F:k]_s` cuenta los homomorfismos de una extensión finita a una clausura algebraica que fijan `k`.

Para extensiones algebraicas generales, `[F:k]_s` admite también cardinalidad infinita. `F^G` es el campo fijo de un subgrupo de automorfismos. Las extensiones de Galois consideradas son finitas, normales y separables; `\gal(F/k)=\Aut_k(F)` y `\gal_k(f)` es el grupo de su campo de descomposición para `f` separable. Los retículos se dibujan con el campo mayor arriba y el subgrupo trivial arriba, por lo que la correspondencia invierte inclusiones. Para un polinomio mónico separable, el discriminante es el cuadrado del producto de las diferencias de sus raíces; el criterio de pertenencia a `A_n` requiere característica distinta de dos.
