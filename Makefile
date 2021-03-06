LATEX    = latex
#BIBTEX   = bibtex
BIBTEX   = biber
DVIPS    = dvips

BASENAME = thesis

default: clean testpdflatex

testlatex:
	latex  ${BASENAME}
	latex  ${BASENAME}
	biber ${BASENAME}
	latex  ${BASENAME}
	latex  ${BASENAME}
	dvipdf -sPAPERSIZE=a4 -dPDFSETTINGS=/prepress ${BASENAME}

testpdflatex:
	pdflatex  ${BASENAME}
	pdflatex  ${BASENAME}
	biber    ${BASENAME}
	pdflatex  ${BASENAME}
	pdflatex  ${BASENAME}
	sh scripts/pages.sh
	
test:
	pdflatex testnote
	pdflatex testnote

#
# standard Latex targets
#

%.dvi:	%.tex 
	$(LATEX) $<

%.bbl:	%.tex *.bib
	$(LATEX) $*
	$(BIBTEX) $*

%.ps:	%.dvi
	$(DVIPS) $< -o $@

%.pdf:	%.tex
	$(PDFLATEX) $<

.PHONY: clean

clean:
	rm -f *.aux *.log *.bbl *.blg *.brf *.cb *.ind *.idx *.ilg  \
	      *.inx *.dvi *.toc *.out *~ ~* spellTmp 

