# Personalización

La base editorial es el proyecto local de Homotopía Estable: se reutilizan sus títulos, índice, encabezados, banner y los dos gráficos institucionales necesarios. Se mantienen 12 puntos, márgenes de una pulgada, texto NewTX y matemática NewTX con opción `libertine`. La portada se adapta a Álgebra Moderna y a otoño de 2025, con rango de clases y sin una fecha de edición calculada con `\today`.

Los entornos conservan la jerarquía de resultados, definiciones, ejemplos, notas y soluciones. Los ejercicios se destacan en un recuadro burdeos. Se usa `amsthm` directamente, con menos dependencias que el preámbulo de referencia. La bibliografía usa natbib y BibTeX porque Biber no pudo ejecutarse en este equipo.

## Paleta

| Nombre | Color | Uso |
| --- | --- | --- |
| `rojoCIMAT` | `#6F263D` | Identidad institucional, recuadros y cierre de pruebas |
| `grisCIMAT` | `#888B8D` | Índice, separadores y aristas secundarias |
| `azulAlgebra` | `#244A73` | Estructura de diagramas y contornos geométricos |
| `acentoAlgebra` | igual a `rojoCIMAT` | Anotaciones rojas, mediadores y recorridos destacados |
| `verdeAlgebra` | `#376B63` | Sectores geométricos que deben distinguirse |
| `ocreAlgebra` | `#9A6B25` | Sectores geométricos que deben distinguirse |

Las primeras tres clases usan sobre todo azul para la escritura y rojo para anotaciones, subrayados, evaluaciones y recorridos. No se observa una regla universal «rojo = mapa canónico». Las etiquetas y los trazos distinguen funciones además del color; no se hereda la regla cromática de Homotopía. Los sectores del hexágono emplean mezclas claras de la paleta y una marca F asimétrica para diferenciar rotaciones y reflexiones. Las líneas de los ejes y el camino en el árbol se destacan en burdeos.

## Símbolos

`Simbolos.tex` define sólo operadores y categorías utilizados: `\Hom`, `\Aut`, `\Sym`, `\im`, `\mcd`, `\mcm`, `\Ob`, `\Set`, `\Grp`, `\Ab` y el delimitador `\generado`. Se conserva la notación ordinaria `\mathbb Z/n\mathbb Z`, `\varphi`, `\ker`, etc.; no se reemplazan operadores estándar ni se introducen abreviaturas de homotopía.

Las clases iniciales no fijan aún convenciones sobre anillos unitarios, cuerpos, ideales o módulos. En su momento se usarán expresiones explícitas como `R`, `K`, `\mathfrak a`, `R/\mathfrak a` y `\Hom_R(M,N)`, contrastando siempre los materiales. No anticipar hipótesis de conmutatividad, unidad o lateralidad.
