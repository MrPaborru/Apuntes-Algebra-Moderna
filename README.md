# Apuntes de Álgebra Moderna

Apuntes personales en español del curso **Álgebra Moderna (18ALG01), CIMAT, otoño de 2025**, impartido por el **Dr. José Luis León Medina**. Alumno: **Pablo Jair Aranda Pérez**.

El curso se impartió en línea, los martes y jueves de 8:00 a 9:20, con Victor Adrián Meza Campa como ayudante. [Información y materiales del curso](https://www.cimat.mx/~luis.leon/es/cursos/algebra-moderna-cimat/).

Las tareas del curso están en el repositorio [Tareas de Álgebra Moderna](https://github.com/MrPaborru/Tareas-Algebra-Moderna).

## Contenido

El documento actualizado se encuentra en [**build/main.pdf**](build/main.pdf). Están completas las **clases 1–6**, del **12, 14, 19, 21 y 26 de agosto y del 4 de septiembre de 2025**, elaboradas a partir de las 74 páginas de sus pizarras. Contiene conjuntos, funciones, categorías, grupos, productos, acciones, grupos libres y abelianos libres, subgrupos, cocientes, el primer teorema de isomorfismo, la ecuación de clases, normalizadores y el teorema de Cauchy, con demostraciones, diagramas y soluciones de las comprobaciones propuestas. La numeración de clases es editorial, por orden cronológico de los archivos conservados; no se atribuye a una numeración original del profesor.

## Organización

- `main.tex`: documento principal.
- `Apuntes/Cuerpo.tex` y `Apuntes/Cn.tex`: integración y un archivo por clase.
- `Personalizacion/`: datos académicos, paleta, símbolos, entornos, títulos, índice y encabezados.
- `Portada/`: portada, banner y los dos PDF gráficos definitivos del CIMAT, procedentes de la plantilla local de Homotopía Estable.
- `Figuras/`: figuras vectoriales definitivas, incluidas desde el documento.
- `Referencias.bib`: referencias verificadas; los localizadores de Aluffi se cotejaron en los fragmentos originales incluidos en las pizarras. Para la reducción de palabras se consultó además el original público de Milne.
- `Recursos/`: pizarras originales locales, intactas y excluidas de la publicación inicial.
- `build/main.pdf`: único producto de compilación destinado a lectura y sincronización.

## Compilación

Los auxiliares se guardan en `build/aux/`. El PDF de lectura es `build/main.pdf`.

Se necesita TeX Live o equivalente, con **pdfLaTeX, latexmk, Perl y BibTeX**. Los paquetes incluyen `newtxtext`, `newtxmath`, `microtype`, `babel` con español, AMS, `mathtools`, TikZ/`tikz-cd`, `tcolorbox`, `titlesec`, `tocloft`, `fancyhdr`, `hyperref`, `natbib`, `cleveref`, `aliascnt` y `refcount`. La bibliografía utiliza BibTeX con `plainnat`.

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
