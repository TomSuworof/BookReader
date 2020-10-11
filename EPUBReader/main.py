from EPUBReader.epub_reader import EPUBReader
import pyttsx3


if __name__ == "__main__":
    book = EPUBReader("the_book_about_hackers.epub")
    book_text = book.convert()

    speaker = pyttsx3.init()
    # voices = speaker.getProperty("voices")
    # print(voices)
    # speaker.setProperty("voice", voices[0].id)
    # speaker.setProperty("rate", 150)

    speaker.say(book_text)
    speaker.runAndWait()
    speaker.stop()
