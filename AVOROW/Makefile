# Makefile for A Vindication of the Rights of Woman by Mary Wollstonecraft
# Translated by neofob from the Project Gutenberg's edition
# Filename: pg3420.txt
# Fonts: Adobe Garamond Premier Pro or Adobe Minion Pro
# These are two good fonts that support UTF-8 with Vietnamese diacritics.

HTMLIZER=maruku
DIRS=en

DOCS:=$(patsubst %.md,%.html,$(wildcard *.md))

all: project sub_dirs

project: $(DOCS)

sub_dirs:
	@echo 'Generating html in subdirectories'
	@for d in $(DIRS); do (make -C $$d project >/dev/null); done

%.html:%.md
	@$(HTMLIZER) $< >/dev/null

clean:
	@echo 'Cleaning html files in $(shell pwd)'
	@rm -f $(DOCS) >/dev/null
distclean: clean
	@for d in $(DIRS); do (make -C $$d clean >/dev/null); done
