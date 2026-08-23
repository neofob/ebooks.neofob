# Makefile for "Trong Gọng Kềm Lịch Sử", Bùi Diễm & David Chanoff
G0=thodan.html modau.html Ch00.html Ch01.html Ch02.html
G1=Ch03.html Ch04.html Ch05.html Ch06.html Ch07.html
G2=Ch08.html Ch09.html Ch10.html Ch11.html Ch12.html
G3=Ch13.html Ch14.html Ch15.html Ch16.html Ch17.html
G4=Ch18.html Ch19.html Ch20.html Ch21.html Ch22.html
G5=Ch23.html Ch24.html Ch25.html Ch26.html Ch27.html
G6=Ch28.html Ch29.html Ch30.html Ch31.html Ch32.html
G7=Ch33.html Ch34.html Ch35.html Ch36.html mucluc.html
MISC=index.html README.html LICENSE.html
ALL=$(G0) $(G1) $(G2) $(G3) $(G4) $(G5) $(G6) $(G7) $(MISC)
all: $(ALL)

# Translator: Phan Lê Dũng
# Typesetter: neofob

#------------------------oOo-------------------------
thodan.html: thodan.txt
	cp thodan.txt thodan.html

modau.html: modau.txt
	htmlizer.pl -t="Mở Đầu" modau.txt

Ch00.html: Ch00.txt
	htmlizer.pl -t="Lời Nói Đầu" Ch00.txt

Ch01.html: Ch01.txt
	htmlizer.pl -t="Chương 1 - Gọng Kềm Lịch Sử" Ch01.txt

Ch02.html: Ch02.txt
	htmlizer.pl -t="Thủơ Ấu Thời" Ch02.txt

#------------------------oOo-------------------------
Ch03.html: Ch03.txt
	htmlizer.pl -t="Những Tổ Chức Chính Trị Bí Mật" Ch03.txt

Ch04.html: Ch04.txt
	htmlizer.pl -t="Đảng Đại Việt" Ch04.txt

Ch05.html: Ch05.txt
	htmlizer.pl -t="Cách Mạng Tháng 08" Ch05.txt

Ch06.html: Ch06.txt
	htmlizer.pl -t="Anh, Tàu, và Pháp" Ch06.txt

Ch07.html: Ch07.txt
	htmlizer.pl -t="Khủng Bố" Ch07.txt

#------------------------oOo-------------------------
Ch08.html: Ch08.txt
	htmlizer.pl -t="Trong Vòng Trốn Tránh" Ch08.txt

Ch09.html: Ch09.txt
	htmlizer.pl -t="Giải Pháp Bảo Đại" Ch09.txt

Ch10.html: Ch10.txt
	htmlizer.pl -t="Mùa Nghỉ Alpine" Ch10.txt

Ch11.html: Ch11.txt
	htmlizer.pl -t="Lập Trường Ngoan Cố Của Pháp" Ch11.txt

Ch12.html: Ch12.txt
	htmlizer.pl -t="Sự Lựa Chọn của Cựu Hoàng" Ch12.txt

#------------------------oOo-------------------------
Ch13.html: Ch13.txt
	htmlizer.pl -t="Ông Diệm và Các Thành Phần Đối Lập" Ch13.txt

Ch14.html: Ch14.txt
	htmlizer.pl -t="Đảo Chánh" Ch14.txt

Ch15.html: Ch15.txt
	htmlizer.pl -t="Tình Hình Sau Đảo Chánh" Ch15.txt

Ch16.html: Ch16.txt
	htmlizer.pl -t="Chính Quyền Tướng Khánh" Ch16.txt

Ch17.html: Ch17.txt
	htmlizer.pl -t="Sự Can Thiệp Của Hoa Kỳ" Ch17.txt

#------------------------oOo-------------------------
Ch18.html: Ch18.txt
	htmlizer.pl -t="Bác Sĩ Quát và Các Tướng Lãnh" Ch18.txt

Ch19.html: Ch19.txt
	htmlizer.pl -t="Con Đường Dẫn Đến Hiến Pháp" Ch19.txt

Ch20.html: Ch20.txt
	htmlizer.pl -t="Bước Thứ Hai" Ch20.txt

Ch21.html: Ch21.txt
	htmlizer.pl -t="Đại Sứ Tại Hoa Thịnh Đốn" Ch21.txt

Ch22.html: Ch22.txt
	htmlizer.pl -t="Hiến Pháp Dân Chủ" Ch22.txt

#------------------------oOo-------------------------
Ch23.html: Ch23.txt
	htmlizer.pl -t="Khung Cảnh Hậu Trường" Ch23.txt

Ch24.html: Ch24.txt
	htmlizer.pl -t="Cuộc Bầu Cử 1967" Ch24.txt

Ch25.html: Ch25.txt
	htmlizer.pl -t="Sự Chuyển Đổi Của Thời Cuộc" Ch25.txt

Ch26.html: Ch26.txt
	htmlizer.pl -t="Tết Mậu Thân" Ch26.txt

Ch27.html: Ch27.txt
	htmlizer.pl -t="Cuộc Đàm Phán Bắt Đầu" Ch27.txt

#------------------------oOo-------------------------
Ch28.html: Ch28.txt
	htmlizer.pl -t="Vụ Anna Chennault" Ch28.txt

Ch29.html: Ch29.txt
	htmlizer.pl -t="Tổng Thống Mới, Chính Sách Mới" Ch29.txt

Ch30.html: Ch30.txt
	htmlizer.pl -t="Trì Hoãn" Ch30.txt

Ch31.html: Ch31.txt
	htmlizer.pl -t="Mất Tiên Cơ" Ch31.txt

Ch32.html: Ch32.txt
	htmlizer.pl -t="Cuộc Độc Cử" Ch32.txt

#------------------------oOo-------------------------
Ch33.html: Ch33.txt
	htmlizer.pl -t="Hai Màn Ngoạn Mục" Ch33.txt

Ch34.html: Ch34.txt
	htmlizer.pl -t="Hiệp Định Ba Lê" Ch34.txt

Ch35.html: Ch35.txt
	htmlizer.pl -t="Những Việc Cuối Cùng" Ch35.txt

Ch36.html: Ch36.txt
	htmlizer.pl -t="Lời Hậu Luận" Ch36.txt

# This is manually html-coded, pre-Markdown era
mucluc.html: mucluc.txt
	cp mucluc.txt mucluc.html
index.html: index.txt
	htmlizer.pl -t="In the Jaws of History" index.txt
README.html: README.md
	maruku README.md

LICENSE.html: LICENSE.md
	maruku LICENSE.md

clean:
	rm -f mucluc.html thodan.html modau.html Ch??.html
