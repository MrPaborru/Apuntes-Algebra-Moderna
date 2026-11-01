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

Las tareas del curso están en el repositorio [Tareas de Álgebra Moderna](https://github.com/MrPaborru/Tareas-Algebra-Moderna).

## Contenido

Los apuntes se organizan en **cinco capítulos numerados**, comenzando por Preliminares.

| Bloque | Contenido |
| --- | --- |
| 1. Preliminares | Conjuntos y lógica; equivalencias, funciones y cocientes; categorías y propiedades universales; orden, Zorn y elección. |
| 2. Teoría de grupos | Grupos y homomorfismos; grupos libres, subgrupos y cocientes; permutaciones y acciones; Cauchy y Sylow; composición, simplicidad y resolubilidad; productos y clasificación abeliana. |
| 3. Teoría de anillos | Anillos y álgebras; polinomios y propiedades universales; ideales y cocientes; primos y maximales; factorización, dominios principales y Euclides; fracciones, Gauss e irreducibilidad. |
| 4. Teoría de módulos | Módulos, cocientes y exactitud; módulos libres, bases y torsión; noetherianidad e Hilbert; clasificación sobre dominios de ideales principales y forma de Smith. |
| 5. Teoría de campos y de Galois | Extensiones simples y algebraicas; clausuras y normalidad; separabilidad y elemento primitivo; campos fijos y correspondencia de Galois; campos finitos y discriminantes. |

Los **211 resultados numerados** comparten un contador por capítulo y los **45 ejercicios resueltos** tienen su propio contador por capítulo. Cada ejercicio incluye su solución completa inmediatamente después del enunciado. Las definiciones y los ejemplos se numeran por sección. Las orientaciones bibliográficas cierran cada capítulo.

El orden sigue las dependencias de las demostraciones: los grupos libres preceden a la generación de subgrupos; las álgebras y la propiedad universal de polinomios se introducen en anillos; el teorema de Hilbert y sus aplicaciones aparecen después de los módulos noetherianos.

## Bibliografía

- Paolo Aluffi, *Algebra: Chapter 0*, Graduate Studies in Mathematics 104, American Mathematical Society, 2009. [DOI](https://doi.org/10.1090/gsm/104).
- James S. Milne, *Group Theory*, versión 4.01, 2025. [Texto del autor](https://www.jmilne.org/math/CourseNotes/GT.pdf).

## Fuentes y compilación

El documento principal es `main.tex`. Los fuentes se organizan por temas en `Apuntes/Preliminares/`, `Apuntes/Grupos/`, `Apuntes/Anillos/`, `Apuntes/Modulos/` y `Apuntes/Campos/`, las figuras vectoriales en `Figuras/`, la portada en `Portada/` y la bibliografía en `Referencias.bib`. Las fuentes LaTeX necesarias para reproducir el documento están incluidas en el repositorio.

Se necesita una distribución TeX con **pdfLaTeX, latexmk, Perl y BibTeX**, además de los paquetes utilizados en el preámbulo. La tipografía utiliza **NewTX**, **LXfonts** para `\mathbb` y **eucal** para `\mathcal`. Los diagramas se componen con TikZ y `tikz-cd`.

Desde la raíz del proyecto:

```sh
latexmk -pdf main.tex
```

En PowerShell también puede utilizarse:

```powershell
.\Compilar.ps1
```

La compilación guarda los archivos auxiliares en `build/aux/` y actualiza `build/main.pdf` cuando termina correctamente. Para eliminar los auxiliares, ejecutar `latexmk -c main.tex` o `.\Compilar.ps1 -Limpiar`.

La configuración del formato, la paleta y los comandos matemáticos se describe en [Personalizacion/README.md](Personalizacion/README.md).
