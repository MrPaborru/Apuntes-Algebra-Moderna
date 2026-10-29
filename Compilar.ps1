param([switch]$Limpiar)
$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    if ($Limpiar) {
        & latexmk -c main.tex
    } else {
        & latexmk -pdf main.tex
        if ($LASTEXITCODE -ne 0) { throw 'La compilación falló; el PDF de lectura no se ha actualizado.' }
        Copy-Item -LiteralPath 'build/aux/main.pdf' -Destination 'build/main.pdf' -Force
    }
    if ($LASTEXITCODE -ne 0) { throw 'latexmk devolvió un error.' }
} finally { Pop-Location }
