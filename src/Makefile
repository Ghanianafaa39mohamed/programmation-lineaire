# Thomas Clavier <https://github.com/tclavier>
# Modif. by Nicolas Mauger <https://github.com/maugern>
# My generic LaTeX Makefile
# 7 dec. 2016

CLEAN_LOG=*~ *.rtf *.ps *.log *.aux *.out *.css *.bak *.toc *.pl *.4ct *.4tc *.lg *.sxw *.tmp *.xref *.idv *.tns *.nav *.snm
CLEAN_OUTPUT=*.pdf *.dvi *.html
# Use ":=" when the variable's definition need to resolve others variables
TEXFILES := $(wildcard *.tex)
# To not compile the includes files !
TEXFILES := $(filter-out *.tex, $(TEXFILES))
SVGFILES = $(wildcard includes/*.svg)

all: pdf

%.pdf: %.tex
	pdflatex  $<
	pdflatex  $<

# Read inkscape manual page for more information
%.png: %.svg
	inkscape -f $< -e $@

clean:
	-rm -f $(CLEAN_LOG)

mrproper:
	-rm -f $(CLEAN_LOG) $(CLEAN_OUTPUT)

png: $(patsubst %.svg,%.png,$(SVGFILES))
pdf: png $(patsubst %.tex,%.pdf,$(TEXFILES))
