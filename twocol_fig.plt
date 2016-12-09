reset

set terminal epslatex size 8.6cm,6cm color colortext standalone header\
 "\\newcommand{\\ft}[0]{\\footnotesize}"
set output 'file.tex'

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5

set tics front 
unset key

#set label 'a)' at screen 0.,0.98
set format x '\ft %g'
set format y '\ft %g'

plot 'file.dat' w lines ls 1

set output

system('latex file.tex && dvips file.dvi && ps2pdf file.ps')
system('mv file.ps nombre.eps')
unset terminal
