# Makefile for Future of Freedom -- Fareed Zarakia
# Translator: {bums,Diễn Vỹ} @ x-cafevn.org
# Page layout: neofob
# PDF: rendered by Cairo plugin in Iceweasel
# Suggested font: Adobe Garamond Premier Pro

MISC=index.html DanNhap.html README.html LICENSE.html
CH=Ch1.html Ch2.html Ch3.html Ch4.html Ch5.html Ch6.html

all: $(MISC) $(CH)

index.html: index.txt
	htmlizer.pl -a="Bums" -t="Mục Lục" index.txt

DanNhap.html: DanNhap.txt
	htmlizer.pl -a="Bums" -t="Lời người dịch - Bums" DanNhap.txt

Ch1.html: Ch1.txt
	htmlizer.pl -a="Fareed Zakaria" -t="Chương Một - Thời Đại Dân Chủ" Ch1.txt

Ch2.html: Ch2.txt
	htmlizer.pl -a="Fareed Zakaria" -t="Chương Hai - Trên Những Con Đường Quanh Co" Ch2.txt

Ch3.html: Ch3.txt
	htmlizer.pl -a="Fareed Zakaria" -t="Chương Ba - Dân Chủ Không Có Tự Do" Ch3.txt

Ch4.html: Ch4.txt
	htmlizer.pl -a="Fareed Zakaria" -t="Chương Bốn - Hồi Giáo, Trường Hợp Đặc Biệt" Ch4.txt

Ch5.html: Ch5.txt
	htmlizer.pl -a="Fareed Zakaria" -t="Chương Năm - Tốt Quá Nên Hóa Xấu" Ch5.txt

Ch6.html: Ch6.txt
	htmlizer.pl -a="Fareed Zakaria" -t="Chương Sáu - Sự Cáo Chung Của Quyền Thế" Ch6.txt

README.html: README.md
	maruku README.md

LICENSE.html: LICENSE.md
	maruku LICENSE.md

clean:
	rm -f $(MISC) $(CH)
