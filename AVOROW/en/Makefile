# Makefile for A Vindication of the Rights of Woman by Mary Wollstonecraft
# Translated by neofob from the Project Gutenberg's edition
# Filename: pg3420.txt
# Fonts: Adobe Garamond Premier Pro or Adobe Minion Pro
# These are two good fonts that support UTF-8 with Vietnamese diacritics.

PDFIZER=sile

DOCS:=$(patsubst %.sil,%.pdf,$(wildcard *.sil))
REQS:=requirements.sil

all: project

project: $(DOCS)

%.pdf:%.sil
	$(PDFIZER) -I $(REQS) $<

clean:
	@echo 'Cleaning pdf files in $(shell pwd)'
	@rm -f $(DOCS) >/dev/null
