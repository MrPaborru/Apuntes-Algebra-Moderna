$ENV{'TZ'} = 'America/Mexico_City';
$ENV{'LC_ALL'} = 'C';
use File::Path qw(make_path);
use File::Copy qw(copy);
$out_dir = 'build/aux';
$aux_dir = 'build/aux';
make_path($out_dir, 'build');
@default_files = ('main.tex');
$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 %O %S';
$max_repeat = 6;
$pdf_previewer = '';
# Hook de latexmk: sólo publica después de una compilación satisfactoria.
$success_cmd = 'perl -e "use File::Copy; copy(\'build/aux/main.pdf\',\'build/main.pdf\') or die $!;"';
$clean_ext = 'synctex.gz run.xml bbl blg';
