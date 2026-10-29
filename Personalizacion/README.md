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

`Simbolos.tex` define sólo operadores y categorías utilizados: `\Hom`, `\Aut`, `\Sym`, `\im`, `\mcd`, `\mcm`, `\Ob`, `\Set`, `\Grp`, `\Ab` y el delimitador `\generado`. Se conserva la notación ordinaria `\mathbb Z/n\mathbb Z`, `\varphi`, `\ker`, etc.; no se reemplazan operadores estándar ni se introducen abreviaturas de homotopía.

Las clases iniciales no fijan aún convenciones sobre anillos unitarios, cuerpos, ideales o módulos. En su momento se usarán expresiones explícitas como `R`, `K`, `\mathfrak a`, `R/\mathfrak a` y `\Hom_R(M,N)`, contrastando siempre los materiales. No anticipar hipótesis de conmutatividad, unidad o lateralidad.
