# Makefile for "A mosinese Mosaic" by Bette Bao Lord
# Translated by Phan Lê Dũng
# Page layout: neofob
# PDF: rendered by Cairo plugin in Iceweasel
# Fonts: Adobe Garamond Premier Pro, Linux Biolinum Capitals O

G0=index.html modau.html mos00.html mos01.html mos02.html
G1=mos03.html mos04.html mos05.html mos06.html mos07.html
G2=mos08.html mos09.html mos10.html mos11.html mos12.html
G3=mos13.html mos14.html mos15.html mos16.html mos17.html
G4=mos18.html mos19.html mucluc.html
MISC=README.html LICENSE.html
ALL=$(G0) $(G1) $(G2) $(G3) $(G4) $(MISC)

all: $(ALL)

#-----------------------------oOo---------------------------
index.html: index.txt
	htmlizer.pl -t="Nét Chấm Phá Của Bức Điêu Khắc Truyền Thần" index.txt

mucluc.html: mucluc.txt
	cp mucluc.txt mucluc.html

modau.html: modau.txt
	htmlizer.pl -t="Lời Người Dịch" modau.txt

mos00.html: mos00.txt
	htmlizer.pl -t="chuyển tiếp" mos00.txt
	
mos01.html: mos01.txt
	htmlizer.pl -t="băng trắng, băng đỏ" mos01.txt

#-----------------------------oOo---------------------------
mos02.html: mos02.txt
	htmlizer.pl -t="nữ diễn viên" mos02.txt

mos03.html: mos03.txt
	htmlizer.pl -t="người học giả" mos03.txt

mos04.html: mos04.txt
	htmlizer.pl -t="gã hề" mos04.txt

mos05.html: mos05.txt
	htmlizer.pl -t="cựu chiến binh của cuộc vạn lý trường chinh" mos05.txt

mos06.html: mos06.txt
	htmlizer.pl -t="du học sinh hồi hương" mos06.txt

#-----------------------------oOo---------------------------
mos07.html: mos07.txt
	htmlizer.pl -t="hòn gạch" mos07.txt

mos08.html: mos08.txt
	htmlizer.pl -t="Người Ký Giả" mos08.txt

mos09.html: mos09.txt
	htmlizer.pl -t="nông gia" mos09.txt

mos10.html: mos10.txt
	htmlizer.pl -t="người tiểu thương" mos10.txt

mos11.html: mos11.txt
	htmlizer.pl -t="kẻ khẩn cầu" mos11.txt

#-----------------------------oOo---------------------------
mos12.html: mos12.txt
	htmlizer.pl -t="bạch khuyển" mos12.txt

mos13.html: mos13.txt
	htmlizer.pl -t="cán bộ" mos13.txt

mos14.html: mos14.txt
	htmlizer.pl -t="người hoạt náo viên" mos14.txt

mos15.html: mos15.txt
	htmlizer.pl -t="những bức chân dung" mos15.txt

mos16.html: mos16.txt
	htmlizer.pl -t="những chuyến ra đi" mos16.txt

#-----------------------------oOo---------------------------
mos17.html: mos17.txt
	htmlizer.pl -t="số mệnh" mos17.txt

mos18.html: mos18.txt
	htmlizer.pl -t="chiếc diều đuôi dài" mos18.txt

mos19.html: mos19.txt
	htmlizer.pl -t="điệp khúc" mos19.txt

README.html: README.md
	maruku README.md

LICENSE.html: LICENSE.md
	maruku LICENSE.md

clean:
	rm -f $(ALL)
