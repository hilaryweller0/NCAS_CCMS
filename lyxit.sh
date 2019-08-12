#!/bin/bash -e

file=WellerSSnotes

echo Creating the online version without answers
sed 's/%VERSION/\\onlineversionWithout/g' studentVersionTMP > studentVersion.tex
lyx --export pdflatex -f all ${file}.lyx
pdflatex -halt-on-error ${file}.tex > /dev/null
bibtex $file
pdflatex -halt-on-error ${file}.tex > /dev/null
mv ${file}.pdf output/${file}_onlineWithout.pdf

echo Creating the students version
sed 's/%VERSION/\\studentversion/g' studentVersionTMP > studentVersion.tex
lyx --export pdflatex -f all ${file}.lyx
pdflatex -halt-on-error ${file}.tex > /dev/null
bibtex $file
pdflatex -halt-on-error ${file}.tex > /dev/null
pdfjam --nup 1x2 --scale 0.95 --a4paper $file.pdf --outfile output/${file}_2_student.pdf > /dev/null

echo Creating the lecturer version
sed 's/%VERSION/\\lecversion/g' studentVersionTMP > studentVersion.tex
lyx --export pdflatex -f all ${file}.lyx
pdflatex -halt-on-error ${file}.tex > /dev/null
bibtex $file
pdflatex -halt-on-error ${file}.tex > /dev/null
pdfjam --nup 1x2 --scale 0.95 --a4paper $file.pdf --outfile output/${file}_2_lec.pdf > /dev/null

rmtexall ${file}.tex

# Copy to dropbox
cp output/* ~/Dropbox/teaching/MPECDT_summerSchool

echo All done
