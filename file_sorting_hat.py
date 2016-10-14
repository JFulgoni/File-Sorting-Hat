__author__ = 'johnfulgoni'

import shutil
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
import string
from nltk.corpus import stopwords
import nltk

en_stopwords = stopwords.words('english')

def pdf_parser(data):
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

if __name__ == '__main__':
    #source_file = sys.argv[1]
    source_file = 'Data/SampleFinal.pdf'
    pdf_result = pdf_parser(source_file)
    print pdf_result

# from here, you can do a smart analysis using nearest neighbor
# or just base it on if then
# then suggest the result, then whether or not you want to move it
# if yes, then use: shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")