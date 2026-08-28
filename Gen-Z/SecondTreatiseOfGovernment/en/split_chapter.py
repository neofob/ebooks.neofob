import re

def split_chapters(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of the Preface and the chapters
    # Preface start: search for "PREFACE"
    preface_match = re.search(r'^PREFACE$', content, re.MULTILINE)
    if not preface_match:
        print("Preface not found")
        return

    preface_start = preface_match.start()
    
    # Find all CHAPTER markers
    chapter_matches = list(re.finditer(r'^CHAPTER\. ([IVXLCDM]+)\.$', content, re.MULTILINE))
    
    if not chapter_matches:
        print("No chapters found")
        return

    # Extract Preface: from 'PREFACE' until the first 'CHAPTER'
    preface_end = chapter_matches[0].start()
    with open('preface.txt', 'w', encoding='utf-8') as f:
        f.write(content[preface_start:preface_end].strip())
    print("Saved preface.txt")

    # Extract Chapters
    for i in range(len(chapter_matches)):
        start = chapter_matches[i].start()
        # End is start of next chapter or end of file
        end = chapter_matches[i+1].start() if i + 1 < len(chapter_matches) else len(content)
        
        roman_num = chapter_matches[i].group(1)
        filename = f"Ch-{roman_num}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content[start:end].strip())
        print(f"Saved {filename}")

if __name__ == "__main__":
    split_chapters('pg7370.txt')
