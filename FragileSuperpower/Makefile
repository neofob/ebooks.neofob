# Makefile for China: Fragile Superpower by Susan L. Shirk
# Translator: Tuan T. Pham

MD_DOCS:=$(patsubst %.md,%.html,$(wildcard *.md))

OUTPUT=$(MD_DOCS)

all: $(OUTPUT)

################################################################################

%.html:%.md
	@maruku $< >/dev/null

clean:
	rm -fr $(OUTPUT)
