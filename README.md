# Apuntes de Álgebra Moderna

Apuntes personales en español del curso **Álgebra Moderna (18ALG01), CIMAT, otoño de 2025**, impartido por el **Dr. José Luis León Medina**. Alumno: **Pablo Jair Aranda Pérez**.

El curso se impartió en línea, los martes y jueves de 8:00 a 9:20, con Victor Adrián Meza Campa como ayudante. [Información y materiales del curso](https://www.cimat.mx/~luis.leon/es/cursos/algebra-moderna-cimat/).

Las tareas del curso están en el repositorio [Tareas de Álgebra Moderna](https://github.com/MrPaborru/Tareas-Algebra-Moderna).

## Contenido

El documento actualizado se encuentra en [**build/main.pdf**](build/main.pdf). Están completas las **clases 1–19**, del **12, 14, 19, 21 y 26 de agosto; del 4, 9, 11, 18, 23, 25 y 30 de septiembre; y del 2, 7, 9, 14, 16, 23 y 30 de octubre de 2025**, elaboradas a partir de las **225 páginas** de sus pizarras. Contiene conjuntos, funciones, categorías, grupos, productos, acciones, grupos libres y abelianos libres, subgrupos, cocientes e isomorfismos, la ecuación de clases, Cauchy y Sylow, Jordan–Hölder, conmutadores y resolubilidad, grupos simétricos y alternantes, extensiones y productos semidirectos, y la clasificación de grupos abelianos finitos. Las clases 11–13 incorporan anillos, unidades, polinomios, endomorfismos, ideales y cocientes, característica, ideales primos y maximales, espectros e introducción a módulos y álgebras. Las clases 14–16 desarrollan submódulos e isomorfismos, productos y coproductos, objetos libres, módulos noetherianos, álgebras finitas y de tipo finito, el teorema de la base de Hilbert, divisibilidad, irreducibles y factorización única, máximos comunes divisores y dominios euclidianos. Las clases 17–19 añaden el algoritmo de Euclides, Zorn y la existencia de ideales maximales, contenido y lema de Gauss, campos de fracciones, factorialidad de anillos de polinomios, raíces, extensiones de campos, cierre algebraico, reducción modular y la forma general de Eisenstein. Incluye las demostraciones desarrolladas en las fuentes, diagramas y soluciones de las comprobaciones propuestas; se indica cuándo un resultado fundacional o el teorema fundamental del álgebra sólo se enuncia. Los complementos necesarios y las correcciones de las pizarras se identifican con sus páginas de origen. La numeración de clases es editorial, por orden cronológico de los archivos conservados; no se atribuye a una numeración original del profesor.

## Organización

- `main.tex`: documento principal.
- `Apuntes/Cuerpo.tex` y `Apuntes/Cn.tex`: integración y un archivo por clase.
- `Personalizacion/`: datos académicos, paleta, símbolos, entornos, títulos, índice y encabezados.
- `Portada/`: portada, banner y los dos PDF gráficos definitivos del CIMAT, procedentes de la plantilla local de Homotopía Estable.
- `Figuras/`: figuras vectoriales definitivas, incluidas desde el documento.
- `Referencias.bib`: referencias verificadas; los localizadores de Aluffi se cotejaron en los fragmentos originales incluidos en las pizarras. La numeración de capítulos se contrastó con el [índice de la vista editorial](https://books.google.com/books/about/Algebra_Chapter_0.html?id=h4dNEAAAQBAJ): III para anillos y módulos, IV para el segundo estudio de grupos. Para la reducción de palabras se consultó además el original público de Milne.
- `Recursos/`: pizarras originales locales, intactas y excluidas de la publicación inicial.
- `build/main.pdf`: único producto de compilación destinado a lectura y sincronización.

## Compilación

Los auxiliares se guardan en `build/aux/`. El PDF de lectura es `build/main.pdf`.

Se necesita TeX Live o equivalente, con **pdfLaTeX, latexmk, Perl y BibTeX**. Los paquetes incluyen `newtxtext`, `newtxmath`, `eucal`, `microtype`, `babel` con español, AMS, `mathtools`, TikZ/`tikz-cd`, `tcolorbox`, `titlesec`, `tocloft`, `fancyhdr`, `hyperref`, `natbib`, `cleveref`, `aliascnt` y `refcount`. También debe estar instalado **LXfonts**, cuya familia `lmsb` conserva la fuente personalizada de `\mathbb` de la plantilla; `eucal` conserva la caligráfica Euler de `\mathcal`. La bibliografía utiliza BibTeX con `plainnat`.

Desde la raíz del proyecto:

```sh
latexmk -pdf main.tex
```

En PowerShell también se puede ejecutar:

```powershell
.\Compilar.ps1
```

El script comprueba el código de salida y asegura la copia final incluso si latexmk no necesita repetir pasadas. Para limpiar los auxiliares:

```sh
latexmk -c main.tex
```
