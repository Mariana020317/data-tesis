default: build

build:
	pdflatex mydocument.tex
	biber mydocument
	pdflatex mydocument.tex
	pdflatex mydocument.tex

clean:
	-rm *.aux 
	-rm *.log 
	-rm *.lof 
	-rm *.bbl 
	-rm *.blg 
	-rm *.lot 
	-rm *.out 
	-rm *.toc 
	-rm *.bcf 
	-rm *.run.xml 
	-rm *.blx.bib
	-rm *.ccf
