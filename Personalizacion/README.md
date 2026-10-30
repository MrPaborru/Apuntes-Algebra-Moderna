# Personalización

La base editorial es el proyecto local de Homotopía Estable: se reutilizan sus títulos, índice, encabezados, banner y los dos gráficos institucionales necesarios. Se mantienen 12 puntos, márgenes de una pulgada, texto NewTX y matemática NewTX con opción `libertine`. La portada conserva «Apuntes de clase», otoño de 2025 y la clave de la materia, con el recuadro del rango casi idéntico al original: ancho mínimo de 4 cm, borde de 1.5 pt, relleno de 3 pt, numerales a 49 pt, guion corto y texto espaciado CLASES. El pie recupera «Guanajuato, Gto., `\today`. E-mail:», con el correo azul enlazado. La fecha de compilación se distingue del periodo del curso; no se añade un aviso sobre publicación oficial.

Los entornos conservan la jerarquía de resultados, definiciones, ejemplos, notas y soluciones. Los ejercicios se destacan en un recuadro burdeos. Se usa `amsthm` directamente, con menos dependencias que el preámbulo de referencia. La bibliografía usa natbib y BibTeX porque Biber no pudo ejecutarse en este equipo.

Se conservan también las elecciones de alfabetos matemáticos del referente: `\mathbb` con la familia `lmsb` de LXfonts y `\mathcal` con la caligráfica Euler de `eucal`. La fuente principal sigue siendo NewTX; estas personalizaciones se declaran después de cargarla.

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

`Simbolos.tex` conserva los operadores y categorías del curso y recupera las utilidades generales de la plantilla del usuario. No se importan macros específicas de homotopía ni se modifican `\hom`, `\Re`, `\Im` o `\ker`. La fuente personalizada de `\mathbb` sí se conserva exactamente mediante `\DeclareMathAlphabet{\mathbb}{U}{lmsb}{m}{n}`: la familia `lmsb` y la fuente `lmsbm8` pertenecen a **LXfonts**. El comentario antiguo del referente la llamaba Latin Modern, pero el archivo `ulmsb.fd` identifica su procedencia. Esta elección tipográfica se aplica a todo el documento y requiere que LXfonts esté instalado.

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

La redefinición de `\given` queda localizada dentro de `\set` y `\ang`, incluso al anidarlos. Los conjuntos por comprensión se escriben con `\set{...\given...}` desde la clase 1, usando `*` o un tamaño explícito cuando el contenido lo necesita; las clases iniciales también se revisan al recuperar una utilidad de la plantilla. `\en`, `\noten` y `\cont` usan los glifos y el espaciado estándar de esta tipografía, en vez de los ajustes particulares de la plantilla anterior. `\restr` adapta automáticamente la altura de la barra. Se conserva el significado de `\ubar` en la plantilla: **barra superior**. `\aut` y `\ob` son alias de `\Aut` y `\Ob` para evitar notaciones duplicadas.

Como en la plantilla del usuario, `\brack{...}` representa corchetes simples: es una sustitución intencional del comando antiguo de TeX para fracciones sin barra. Si se necesita ese otro uso, escribir `\genfrac{[}{]}{0pt}{}{n}{k}`. No se añaden redefiniciones globales de los operadores estándar.

`Referencias.tex` recupera `\myref{etiqueta}` (tipo y número, más nombre si existe) y `\abvref{etiqueta}` (tipo abreviado y número), mediante `cleveref` y `refcount`. `aliascnt` permite distinguir teoremas, proposiciones, lemas y corolarios aunque compartan numeración. Reconocen los entornos de este curso y llaman «clase» al capítulo. `sol` admite un título opcional, como `\begin{sol}[Otra solución]`. Las notas y observaciones sin número no deben citarse como resultados numerados.

En la portada, el guion corto se compone en una caja propia, fuera de las abreviaturas ordinales y con un pequeño espacio a cada lado, para que permanezca visible.

El recuadro del rango conserva 4 cm como ancho mínimo. Cuando el rango necesita más espacio, se mide con sus numerales de 49 pt y se amplían conjuntamente la caja burdeos y la caja «CLASES», dejando holgura interior. Así caben las cifras y los ordinales de `1ª-10ª` y de rangos posteriores sin desbordamiento ni reducción de la tipografía.

La separación de ese bloque respecto de la temporada/clave y de «Docente» usa una misma longitud, `\SeparacionRangoPortada`, fijada en 2 cm. La separación superior se aumentó para equilibrarla con la inferior.

Desde la clase 11 los anillos tienen unidad y los homomorfismos la preservan; se admite el anillo cero. No se supone conmutatividad salvo indicación. Dominios y campos son no nulos. El fragmento de la definición de anillo de división no excluye expresamente el cero, y esa diferencia se documenta en la clase. Las unidades se escriben `R^\times` (también `R^*` en la pizarra). La fuente llama «unidad por la izquierda» a `u` si `uv=1`: tiene un inverso por la derecha; siempre se explicita la ecuación para evitar intercambiar los nombres. Su definición de divisor de cero permite el elemento cero; los dominios excluyen divisores de cero **no nulos**.

Desde la clase 12, ideal significa bilateral salvo precisión; un ideal propio no contiene la unidad y no es subanillo bajo la convención anterior. Se usan `I`, `(a_1,\ldots,a_n)` y `R/I`, y `\operatorname{char}R` permite característica cero. Las sumas de familias de ideales son sumas **finitas** de elementos. Para polinomios se usa `\deg0=-\infty`; dividir por un mónico no requiere que el anillo sea campo. La identificación `R[x]/(f)\cong R^{\oplus d}` describe grupos aditivos; el producto requiere reducción módulo `f`.

Desde la clase 13, los módulos son izquierdos y unitarios. Se escribe `R\text{-}\mathbf{Mod}`, `\Hom_R(M,N)` y `\End_{\Ab}(M)`, cuyo producto es composición. La estructura de módulo sobre `\Hom_R(M,N)` mediante multiplicación puntual de escalares se afirma para `R` conmutativo. Una `R`-álgebra, con `R` conmutativo, incluye un homomorfismo de imagen central; el anillo de destino puede ser no conmutativo. `\Ring` y `\Spec` dan la categoría de anillos y el espectro, respectivamente; no se redefine ningún operador estándar.

Desde las clases 14–16, `\ang{A}` denota el submódulo generado y `R^{\oplus A}` funciones de soporte finito. La función de generadores libres es inyectiva para `R\ne0`; el anillo cero requiere la excepción descrita en clase 14. Los polinomios `R[A]` dan el álgebra libre en la categoría de **álgebras conmutativas**, con base conmutativa. «Finita» significa finitamente generada como módulo; «de tipo finito», como álgebra, y se explicita la conmutatividad al presentar esta última mediante polinomios conmutativos.

Para dominios, «primo» sigue la convención de la pizarra: `(a)` es primo, por lo que se permite `a=0`; se exige «primo no nulo» para deducir irreducibilidad. DFU traduce UFD; las factorizaciones se comparan salvo orden y asociados, con un factor unidad cuando se fijan representantes. Las multiplicidades se comparan sobre clases de asociados y suman en un producto. `\mcd` en un dominio representa una elección salvo asociados. La función euclidiana se llama `v` y sólo exige la división con resto de menor tamaño; no se le atribuyen otros axiomas de valuación.

Los localizadores de Aluffi usan **III** para anillos y módulos y **IV** para el segundo estudio de grupos. Se corrigió el intercambio de esos números en las clases 6–13 tras cotejar las referencias impresas de las pizarras y el índice editorial. Las secciones y los números de los resultados originales se conservan.

Desde las clases 17–19, `K(R)` es el campo de fracciones de un dominio y `R(x)=K(R[x])` el campo de funciones racionales formales. No confundir las fracciones con funciones definidas en todos los puntos ni, sobre un dominio arbitrario, con funciones de valores en el mismo anillo. Para un DFU, se escribe explícitamente `\operatorname{cont}(f)` y se abrevia `c_f` para un contenido de un polinomio **no nulo** y `C_f=(c_f)` para su ideal, que es canónico. No reutilizar `\cont`, cuyo significado en la plantilla es pertenencia invertida. Los ideales `(f)` en `R[x]` y `(f)_K` en `K[x]` se distinguen al pasar a fracciones. Una extensión de campos es un homomorfismo unitario, automáticamente inyectivo; la unicidad al adjuntar una raíz requiere fijar esa raíz. `\mathbb F_p=\mathbb Z/p\mathbb Z` se usa para `p` primo. La identificación de un cociente por un mónico con sus coeficientes es lineal, y su producto requiere reducir restos. La forma general de Eisenstein conserva su conclusión sobre grados; se explicitan las hipótesis adicionales para deducir irreducibilidad.

En las clases 8–10, `G'=[G,G]` es el subgrupo **generado** por conmutadores `ghg^{-1}h^{-1}`; `G^{\mathrm{ab}}=G/G'` y `G^{(i)}` es la serie derivada. Característico se refiere a automorfismos; plenamente invariante, a endomorfismos. Las series normales requieren normalidad en el término anterior y los factores de composición se cuentan con multiplicidad. El signo se escribe `\varepsilon`, con acción por sustitución a la izquierda y composición de funciones. `N\rtimes_\theta H` usa la operación `(n,h)(m,k)=(n\theta_h(m),hk)`. En la clasificación abeliana se cambia explícitamente a notación aditiva, con neutro cero y sumas directas; los factores invariantes satisfacen `1<d_1\mid\cdots\mid d_s`. El uso de polinomios formales con coeficientes enteros en el signo no introduce aún convenciones generales de anillos o módulos.

En las clases 4–6, `F^{\mathrm{ab}}(A)` se modela con `\mathbb Z^{\oplus A}` (funciones de soporte finito). `G/H` designa el conjunto de clases izquierdas para cualquier subgrupo; sólo se le da estructura de grupo cociente si `H` es normal. Se usa `\Stab_G(a)`, `O_G(a)`, `Z(G)`, `Z_G(A)` y `N_G(A)` para estabilizador, órbita, centro, centralizador y normalizador. Los puntos fijos de una acción en `S` se escriben `S^G`, y `R` reúne representantes de órbitas no triviales, para distinguirlos del centro y del conjunto actuado.
