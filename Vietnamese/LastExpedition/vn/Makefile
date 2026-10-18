# Simple Makefile to generate Final Book
#
BOOK_FONT ?="Garamond Premier Pro"
APPENDIX=Appendix-I-vn.md Appendix-II-vn.md
PREFACE=Preface-vn.md
# Chapter I to IX
CHAPTERS_G0=Ch-I-vn.md Ch-II-vn.md Ch-III-vn.md Ch-IV-vn.md Ch-V-vn.md Ch-VI-vn.md Ch-VII-vn.md Ch-VIII-vn.md Ch-IX-vn.md
# Chapter X to XVIII
CHAPTERS_G1=Ch-X-vn.md Ch-XI-vn.md Ch-XII-vn.md Ch-XIII-vn.md Ch-XIV-vn.md Ch-XV-vn.md Ch-XVI-vn.md Ch-XVII-vn.md Ch-XVIII-vn.md
CHAPTERS=$(CHAPTERS_G0) $(CHAPTERS_G1)
COVER="Cover-vn.md"
GLOSSARY="GLOSSARY.md"
INDEX="INDEX.md"
ALL=${COVER} ${INDEX} ${PREFACE} $(CHAPTERS_G0) $(CHAPTERS_G1) $(APPENDIX) ${GLOSSARY}

all: LastExpedition-vn.md
	pandoc LastExpedition-vn.md -o LastExpedition-vn.pdf --pdf-engine=xelatex -V mainfont=${BOOK_FONT}


LastExpedition-vn.md:
	cat ${ALL} > LastExpedition-vn.md
