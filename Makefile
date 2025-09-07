
# Simple Makefile to build the master PDF and (optionally) the two standalones.

TEX=pdflatex
MASTER=LLM_Bias_Coach_Master.tex
DRAFT=LLM_Bias_Coach_Draft.tex
TWOPAGER=LLM_Bias_Coach_TwoPager.tex

all: master

master:
	$(TEX) -interaction=nonstopmode -file-line-error $(MASTER)
	$(TEX) -interaction=nonstopmode -file-line-error $(MASTER)  # second pass for TOC, refs

draft:
	$(TEX) $(DRAFT)

two:
	$(TEX) $(TWOPAGER)

clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot

distclean: clean
	rm -f LLM_Bias_Coach_Master.pdf LLM_Bias_Coach_Draft.pdf LLM_Bias_Coach_TwoPager.pdf
