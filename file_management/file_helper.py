__author__ = 'johnfulgoni'

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
import string
from nltk.corpus import stopwords
import nltk

en_stopwords = stopwords.words('english')

def parse_pdf(data):
    print 'Parsing PDF data...'
    fp = file(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=(LAParams()))
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    return process_file_string(data)

def process_file_string(data):
    data = data.lower()
    data = nltk.word_tokenize(data.decode('utf-8'))
    data = remove_punctuation(data)
    data = remove_stopwords(data)
    print 'Parsing complete...'
    return data

def remove_punctuation(s):
    result = []
    for word in s:
        if word not in string.punctuation and word != '``':
            result.append(word)

    return result

def remove_stopwords(s):
    result = []
    for word in s:
        if word not in en_stopwords:
            result.append(word)
    return result