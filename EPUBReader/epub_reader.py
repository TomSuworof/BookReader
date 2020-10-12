import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]

# huge respect to ZA3karia, there is his code


class EPUBReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def epub2thtml(self, epub_path):
        book = epub.read_epub(epub_path)
        chapters = []
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item.get_content())
        return chapters

    def chap2text(self, chap):
        output = ''
        soup = BeautifulSoup(chap, 'html.parser')
        text = soup.find_all(text=True)
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)
        return output

    def thtml2ttext(self, thtml):
        output = []
        for html in thtml:
            text = self.chap2text(html)
            output.append(text)
        return output

    def epub2text(self, epub_path):
        chapters = self.epub2thtml(epub_path)
        ttext = self.thtml2ttext(chapters)
        return ttext

    def convert(self):
        text = self.epub2text(self.file_name)
        # for chapter in text:
        #     chapter = chapter.replace('\n', '').replace('\xa0-', '')
        for i in range(len(text)):
            text[i] = text[i].replace('\n', '').replace('\xa0', '')
        return text
