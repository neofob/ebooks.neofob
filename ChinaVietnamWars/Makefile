# Makefile for the Vietnamese translation of
# "China & Vietnam Wars, 1950-1975 Qiang Zhai"
# Translated by Diên Vỹ @ danluan.org
# Fonts: Adobe Garamond Premier Pro or Adobe Minion Pro
# These are two good fonts that support UTF-8 with Vietnamese diacritics.

HTMLIZER=maruku

DOCS:=$(patsubst %.md,%.html,$(wildcard *.md))

all: project

project: $(DOCS)

%.html:%.md
	$(HTMLIZER) $< >/dev/null

clean:
	@echo 'Cleaning html files in $(shell pwd)'
	@rm -f $(DOCS) >/dev/null
