#!/bin/bash -e

file=WellerSSnotes

echo Creating the students version
sed 's/%VERSION/\\studentversion/g' studentVersionTMP > studentVersion.tex
lyx --export pdflatex -f all ${file}.lyx
pdflatex -halt-on-error ${file}.tex
bibtex $file
pdflatex -halt-on-error ${file}.tex > /dev/null
pdfjam --nup 1x2 --scale 0.95 --a4paper $file.pdf --outfile output/${file}_2_student.pdf > /dev/null
cp $file.pdf output/${file}_1_student.pdf
echo Created output/${file}_2_student.pdf

echo Creating the lecturer version
sed 's/%VERSION/\\lecversion/g' studentVersionTMP > studentVersion.tex
lyx --export pdflatex -f all ${file}.lyx; pdflatex -halt-on-error ${file}.tex
bibtex $file
pdflatex -halt-on-error ${file}.tex  > /dev/null
pdfjam --nup 1x2 --scale 0.95 --a4paper $file.pdf --outfile output/${file}_2_lec.pdf > /dev/null
echo Created output/${file}_2_lec.pdf

echo Creating the online version with answers
sed 's/%VERSION/\\onlineversionWith/g' studentVersionTMP > studentVersion.tex; \
lyx --export pdflatex -f all ${file}.lyx; \
pdflatex -halt-on-error ${file}.tex
bibtex $file
pdflatex -halt-on-error ${file}.tex > /dev/null
cp ${file}.pdf ${file}_onlineWith.pdf
echo Created ${file}_onlineWith.pdf

rmtexall ${file}.tex

# Copy to website
scp output/*pdf practicals/testCode.py sws02hs@racc.rdg.ac.uk:/home/users/sws02hs/public_html/teaching/summerSchool/

