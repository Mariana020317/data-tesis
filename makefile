default: build

build:
	pdflatex -interaction=nonstopmode mydocument.tex
	biber mydocument
	pdflatex -interaction=nonstopmode mydocument.tex
	pdflatex -interaction=nonstopmode mydocument.tex

clean:
	-rm *.aux *.log *.lof *.bbl *.blg *.lot *.out *.toc *.bcf *.run.xml *.blx.bib *.ccf *.fls *.fdb_latexmk *.synctex.gz
