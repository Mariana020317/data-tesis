default: build

build:
	pdflatex -interaction=nonstopmode mydocument.tex
	biber mydocument
	pdflatex -interaction=nonstopmode mydocument.tex
	pdflatex -interaction=nonstopmode mydocument.tex

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
