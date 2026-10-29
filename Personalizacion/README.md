# Personalización

La base editorial es el proyecto local de Homotopía Estable: se reutilizan sus títulos, índice, encabezados, banner y los dos gráficos institucionales necesarios. Se mantienen 12 puntos, márgenes de una pulgada, texto NewTX y matemática NewTX con opción `libertine`. La portada conserva «Apuntes de clase», otoño de 2025 y la clave de la materia, con el recuadro del rango casi idéntico al original: ancho de 4 cm, borde de 1.5 pt, relleno de 3 pt, numerales a 49 pt, guion corto y texto espaciado CLASES. El pie recupera «Guanajuato, Gto., `\today`. E-mail:», con el correo azul enlazado. La fecha de compilación se distingue del periodo del curso; no se añade un aviso sobre publicación oficial.

Los entornos conservan la jerarquía de resultados, definiciones, ejemplos, notas y soluciones. Los ejercicios se destacan en un recuadro burdeos. Se usa `amsthm` directamente, con menos dependencias que el preámbulo de referencia. La bibliografía usa natbib y BibTeX porque Biber no pudo ejecutarse en este equipo.

## Paleta

| Nombre | Color | Uso |
| --- | --- | --- |
| `rojoCIMAT` | `#6F263D` | Identidad institucional, recuadros y cierre de pruebas |
| `grisCIMAT` | `#888B8D` | Índice, separadores y rellenos geométricos claros |
| `rojoDiagramaCIMAT` | `#8A1E43` | Énfasis matemático en flechas, recorridos y ejes |
| negro | `#000000` | Flechas, contornos y etiquetas ordinarias |
| `azulAlgebra` | `#244A73` | Sólo sectores geométricos que deben distinguirse |
| `verdeAlgebra` | `#376B63` | Sectores geométricos que deben distinguirse |
| `ocreAlgebra` | `#9A6B25` | Sectores geométricos que deben distinguirse |

Por indicación expresa del usuario, **las flechas se dejan negras por defecto**. El estilo `estructura` conserva ese negro y el estilo `destacado` usa `rojoDiagramaCIMAT`, variante de énfasis de la plantilla de referencia. El color rojo no significa siempre «mapa canónico»; debe destacar una relación, mediador o recorrido concreto. Las etiquetas y los trazos mantienen el significado además del color. Se descarta la decisión inicial de colorear flechas según el azul de la escritura.

Los tonos azul, verde y ocre se conservan únicamente para los sectores del hexágono, donde distinguen las imágenes de las simetrías junto con una marca F asimétrica; son colores auxiliares de ilustración, **no una paleta institucional verificada**. Los ejes y el camino del árbol usan `rojoDiagramaCIMAT`; los contornos y demás aristas son negros. Los triángulos tienen relleno gris claro.

Se consultó el [Manual Básico de Imagen del CIMAT](https://www.cimat.mx/wp-content/uploads/2022/09/Manual-ba%CC%81sico-de-logotipo.pdf), que identifica los colores base Pantone 209 C y Cool Gray 8 C. Los valores de `rojoCIMAT` y `grisCIMAT` se mantienen como en la plantilla solicitada. Sólo se añadirán otros colores institucionales para flechas si es necesario distinguir varios énfasis en un mismo diagrama y después de verificar sus especificaciones; en este bloque bastan negro y rojo.

## Símbolos

`Simbolos.tex` conserva los operadores y categorías del curso y recupera las utilidades generales de la plantilla del usuario. No se importan macros específicas de homotopía ni se modifican `\hom`, `\Re`, `\Im`, `\ker` o `\mathbb`.

| Comandos | Uso |
| --- | --- |
| `\set`, `\given`, `\SetSymbol` | Conjuntos por comprensión con separación y barra ajustable |
| `\ang`, `\generado` | Delimitadores angulares; `\ang` admite `\given` para presentaciones |
| `\brack`, `\Brack`, `\floor`, `\ceil`, `\round` | Corchetes simples o dobles, piso, techo y delimitadores mixtos |
| `\restr`, `\supsub`, `\ubar` | Restricción de una expresión, índices pequeños y barra superior de la plantilla |
| `\en`, `\noten`, `\cont`, `\dotcup` | Pertenencia, no pertenencia, pertenencia inversa y unión disjunta |
| `\bigforall`, `\bigexists`, `\colonequiv` | Cuantificadores ampliados y equivalencia por definición |
| `\Hom`, `\Aut`, `\aut`, `\End`, `\Sym`, `\gal`, `\rk`, `\card`, `\coker` | Operadores algebraicos |
| `\im`, `\mcd`, `\mcm`, `\dom`, `\cod`, `\id`, `\ord`, `\res`, `\supp`, `\ev` | Operadores de funciones y estructuras algebraicas |
| `\Stab` | Estabilizadores de acciones; desde la clase 6 |
| `\Ob`, `\ob`, `\Set`, `\Grp`, `\Ab`, `\Vect`, `\cat`, `\Col` | Objetos, categorías y colecciones |

Los delimitadores admiten tamaño normal, automático con `*` y explícito con `[...]`, por ejemplo:

```latex
\set{x \in G \given x^2=e}
\set*{\frac{a}{b} \given a\in\mathbb Z,\ b\ne0}
\set[\Big]{x\in R \given x\ne0}
\ang{x,y \given x^2=y^3=e}
\floor*{\frac{n}{2}}
\restr{f}{H}
```

La redefinición de `\given` queda localizada dentro de `\set` y `\ang`, incluso al anidarlos. `\en`, `\noten` y `\cont` usan los glifos y el espaciado estándar de esta tipografía, en vez de los ajustes particulares de la plantilla anterior. `\restr` adapta automáticamente la altura de la barra. Se conserva el significado de `\ubar` en la plantilla: **barra superior**. `\aut` y `\ob` son alias de `\Aut` y `\Ob` para evitar notaciones duplicadas.

Como en la plantilla del usuario, `\brack{...}` representa corchetes simples: es una sustitución intencional del comando antiguo de TeX para fracciones sin barra. Si se necesita ese otro uso, escribir `\genfrac{[}{]}{0pt}{}{n}{k}`. No se añaden redefiniciones globales de los operadores estándar.

`Referencias.tex` recupera `\myref{etiqueta}` (tipo y número, más nombre si existe) y `\abvref{etiqueta}` (tipo abreviado y número), mediante `cleveref` y `refcount`. `aliascnt` permite distinguir teoremas, proposiciones, lemas y corolarios aunque compartan numeración. Reconocen los entornos de este curso y llaman «clase» al capítulo. `sol` admite un título opcional, como `\begin{sol}[Otra solución]`. Las notas y observaciones sin número no deben citarse como resultados numerados.

En la portada, el guion corto se compone en una caja propia, fuera de las abreviaturas ordinales y con un pequeño espacio a cada lado, para que permanezca visible.

Las clases iniciales no fijan aún convenciones sobre anillos unitarios, cuerpos, ideales o módulos. En su momento se usarán expresiones explícitas como `R`, `K`, `\mathfrak a`, `R/\mathfrak a` y `\Hom_R(M,N)`, contrastando siempre los materiales. No anticipar hipótesis de conmutatividad, unidad o lateralidad.

En las clases 8–10, `G'=[G,G]` es el subgrupo **generado** por conmutadores `ghg^{-1}h^{-1}`; `G^{\mathrm{ab}}=G/G'` y `G^{(i)}` es la serie derivada. Característico se refiere a automorfismos; plenamente invariante, a endomorfismos. Las series normales requieren normalidad en el término anterior y los factores de composición se cuentan con multiplicidad. El signo se escribe `\varepsilon`, con acción por sustitución a la izquierda y composición de funciones. `N\rtimes_\theta H` usa la operación `(n,h)(m,k)=(n\theta_h(m),hk)`. En la clasificación abeliana se cambia explícitamente a notación aditiva, con neutro cero y sumas directas; los factores invariantes satisfacen `1<d_1\mid\cdots\mid d_s`. El uso de polinomios formales con coeficientes enteros en el signo no introduce aún convenciones generales de anillos o módulos.

En las clases 4–6, `F^{\mathrm{ab}}(A)` se modela con `\mathbb Z^{\oplus A}` (funciones de soporte finito). `G/H` designa el conjunto de clases izquierdas para cualquier subgrupo; sólo se le da estructura de grupo cociente si `H` es normal. Se usa `\Stab_G(a)`, `O_G(a)`, `Z(G)`, `Z_G(A)` y `N_G(A)` para estabilizador, órbita, centro, centralizador y normalizador. Los puntos fijos de una acción en `S` se escriben `S^G`, y `R` reúne representantes de órbitas no triviales, para distinguirlos del centro y del conjunto actuado.
