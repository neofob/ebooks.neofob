# Silly Makefile for the unicode UTF8 html files
# Author: Tuan T. Pham

ALL_DIRS=Future_Of_Freedom JAWS MOSAIC Partners

all:
	-for d in $(ALL_DIRS); do (cd $$d; make all ); done

clean:
	-for d in $(ALL_DIRS); do (cd $$d; make clean ); done
