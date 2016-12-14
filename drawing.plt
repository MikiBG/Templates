reset

# better option if there are no latex labels
#set terminal pdfcairo size 4cm,3cm color 
#set output 'drawing.pdf'
set terminal epslatex size 4cm,4cm color colortext standalone header\
 "\\newcommand{\\ft}[0]{\\footnotesize}"
set output 'file.tex'

unset tics
unset border
set size ratio -1 #to set the same lengthscale in both axis
# use all available space to plot
set lmargin at screen 0.
set rmargin at screen 1.
set tmargin at screen 1.
set bmargin at screen 0.

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5

unset key

#set label 'a)' at screen 0.,0.98

plot 'file.dat' w lines ls 1

set output

system('latex file.tex && dvips file.dvi && ps2pdf file.ps')
system('mv file.ps nombre.eps')
unset terminal
