# Makefile for A Vindication of the Rights of Women by Mary Wollstonecraft
# Translated by neofob from the Project Gutenber's edition
# Filename: pg3420.txt
# Fonts: Adobe Garamond Premier Pro or Adobe Minion Pro
# These two fonts support UTF-8 with Vietnamese diacritics.

HTMLIZER=maruku
MISC=index.html ChanDung.html DanNhap.html
CHAPTERS=Ch-01.html

%.html:%.md
	$(HTMLIZER) $<
clean:
	rm -f $(MISC) $(CHAPTERS)
