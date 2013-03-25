all: README.html

README.html: README.md
	maruku README.md

clean:
	rm -f README.html
