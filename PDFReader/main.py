import pyttsx3
import PyPDF2

if __name__ == '__main__':
    pdfReader = PyPDF2.PdfFileReader(open('java_eckel.pdf', 'rb'))
    pages = pdfReader.numPages
    print(pages)

    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices")
    print(voices)
    speaker.setProperty("voice", voices[2].id)
    speaker.setProperty("rate", 150)

    for page_number in range(pdfReader.numPages):
        print('no we are at page', page_number)
        text_from_page = pdfReader.getPage(page_number).extractText()
        speaker.say(text_from_page)
        speaker.runAndWait()
    speaker.stop()
