# Apuntes de Álgebra Moderna

Apuntes en español para consultar y estudiar los fundamentos de grupos, anillos, módulos y campos. Incluyen definiciones, teoremas con sus demostraciones, ejemplos, diagramas y ejercicios con solución.

**[Leer los apuntes en PDF](build/main.pdf)**

## El curso

**Álgebra Moderna (18ALG01)** · Centro de Investigación en Matemáticas (CIMAT) · **Otoño 2025**.

- **Profesor:** Dr. José Luis León Medina.
- **Ayudante:** Victor Adrián Meza Campa.
- **Modalidad:** en línea.
- **Horario:** martes y jueves, de 8:00 a 9:20.
- **Autor de los apuntes:** Pablo Jair Aranda Pérez.

[Información, temario y materiales del curso](https://www.cimat.mx/~luis.leon/es/cursos/algebra-moderna-cimat/).

## Contenido

La versión actual comprende **22 clases**, del **12 de agosto al 11 de noviembre de 2025**, organizadas en capítulos fechados.

| Clases | Temas |
| --- | --- |
| 1–5 | Conjuntos, funciones y categorías; grupos, simetrías, productos, grupos libres, subgrupos, cocientes y primer teorema de isomorfismo. |
| 6–10 | Acciones y ecuación de clases; Cauchy y Sylow; Jordan–Hölder, resolubilidad, grupos simétricos y alternantes; productos semidirectos y clasificación de grupos abelianos finitos. |
| 11–14 | Anillos, polinomios, ideales y cocientes; característica, ideales primos y maximales; módulos, álgebras, submódulos y construcciones libres. |
| 15–19 | Noetherianidad y teorema de Hilbert; divisibilidad y factorización; dominios euclidianos, Zorn, contenido y lema de Gauss; fracciones, raíces, extensiones e irreducibilidad. |
| 20–22 | Bases, dimensión, rango y torsión; clasificación de módulos sobre un DIP y forma de Smith; extensiones simples, polinomios mínimos y automorfismos de campos. |

Los ejercicios llevan su solución inmediatamente después del enunciado. La numeración de resultados es global; las definiciones y los ejemplos se numeran por sección. Cada clase cierra con referencias para profundizar en los temas tratados.

## Bibliografía

- Paolo Aluffi, *Algebra: Chapter 0*, Graduate Studies in Mathematics 104, American Mathematical Society, 2009. [DOI](https://doi.org/10.1090/gsm/104).
- James S. Milne, *Group Theory*, versión 4.01, 2025. [Texto del autor](https://www.jmilne.org/math/CourseNotes/GT.pdf).

## Fuentes y compilación

El documento principal es `main.tex`. Los capítulos se encuentran en `Apuntes/`, las figuras vectoriales en `Figuras/`, la portada en `Portada/` y la bibliografía en `Referencias.bib`. Las fuentes LaTeX necesarias para reproducir el documento están incluidas en el repositorio.

Se necesita una distribución TeX con **pdfLaTeX, latexmk, Perl y BibTeX**, además de los paquetes utilizados en el preámbulo. La tipografía utiliza **NewTX**, **LXfonts** para `\mathbb` y **eucal** para `\mathcal`. Los diagramas se componen con TikZ y `tikz-cd`.

Desde la raíz del proyecto:

```sh
latexmk -pdf main.tex
```

En PowerShell también puede utilizarse:

```powershell
.\Compilar.ps1
```

La compilación actualiza `build/main.pdf` cuando termina correctamente. Para eliminar los auxiliares, ejecutar `latexmk -c main.tex` o `.\Compilar.ps1 -Limpiar`.

La configuración del formato, la paleta y los comandos matemáticos se describe en [Personalizacion/README.md](Personalizacion/README.md).
