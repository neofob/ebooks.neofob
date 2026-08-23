# Makefile for "Partners in Power" by Robert Dalleck
# Translated by Cymbidum @ x-cafevn.org
# Page layout: neofob
# PDF: rendered by Cairo plugin in Iceweasel
# Font: Adobe Garamond Premier Pro

MISC=index.html DanNhap.html Epilogue.html README.html LICENSE.html
C0=Ch2.html Ch3.html Ch4.html Ch5.html
C1=Ch6.html Ch7.html Ch8.html Ch9.html Ch10.html
C2=Ch11.html Ch12.html Ch13.html Ch14.html Ch15.html
C3=Ch16.html
ALL=$(MISC) $(C0) $(C1) $(C2) $(C3)

all: $(ALL)

index.html: index.txt
	htmlizer.pl -a="Cymbidium" -t="Mục Lục" index.txt

DanNhap.html: DanNhap.txt
	htmlizer.pl -a="Cymbidium" -t="Lời người dịch - Cymbidium" DanNhap.txt

Ch2.html: Ch2.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Hai - Kissinger" Ch2.txt

Ch3.html: Ch3.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Ba - Năm 1968" Ch3.txt

Ch4.html: Ch4.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Bốn - Nixon và Kissinger trong Bạch Ốc" Ch4.txt

Ch5.html: Ch5.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Năm - Hy Vọng và Ảo Vọng" Ch5.txt

Ch6.html: Ch6.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Sáu - Chính Trị Của Chính Sách Ngoại Giao" Ch6.txt

Ch7.html: Ch7.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Bảy - Khó Khăn Triền Miên" Ch7.txt

Ch8.html: Ch8.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Tám - Quản Lý Khủng Hoảng" Ch8.txt

Ch9.html: Ch9.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Chín - Mùa Đông Không Vui" Ch9.txt

Ch10.html: Ch10.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Mười - Con Đường Đến Hòa Bình" Ch10.txt

Ch11.html: Ch11.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Mười Một - Hòa Hoãn Ở Á Châu: Thắng Lợi Và Mất Mát" Ch11.txt

Ch12.html: Ch12.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Mười Hai - Chiến Sĩ Làm Người Hoà Giải" Ch12.txt

Ch13.html: Ch13.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Mười Ba - Chiến Thắng Ô Uế" Ch13.txt

Ch14.html: Ch14.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Mười Bốn - Nỗi Khốn Khổ Mới" Ch14.txt

Ch15.html: Ch15.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Mười Lăm - Bóng Tối Watergate" Ch15.txt

Ch16.html: Ch16.txt
	htmlizer.pl -a="Robert Dalleck" -t="Chương Mười Sáu - Kết Thúc Thời Tổng Thống Nixon-Kissinger" Ch16.txt

Epilogue.html: Epilogue.txt
	htmlizer.pl -a="Robert Dalleck" -t="Lời Bạt" Epilogue.txt

README.html: README.md
	maruku README.md

LICENSE.html: LICENSE.md
	maruku LICENSE.md

clean:
	rm -f $(ALL)
