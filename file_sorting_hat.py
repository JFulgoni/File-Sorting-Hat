__author__ = 'johnfulgoni'

import shutil
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
import string
import nltk

def pdf_parser(data):

    fp = file(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    output =  remove_punctuation(nltk.word_tokenize(data.decode('utf-8')))

    return output

    # output = data.split()
    #
    # # Using clean_word function to clean each word in the list
    # for w in range(len(output)):
    #     output[w] = clean_word(output[w])
    # # Removing all empty strings from list
    # while '' in output:
    #     output.remove('')
    #
    # return output

def remove_punctuation(s):
    result = []
    for word in s:
        if word not in string.punctuation and word != '``':
            result.append(word)

    return result

# Remove whitespace, punctuation, etc. from a word; turn it into a lower case
# string with only alphanumeric characters.
# def clean_word(word):
#     if type(word) is str:
#         return filter(str.isalpha, word).lower()
#     elif type(word) is unicode:
#         # Normalize unicode and turn it into ASCII
#         non_unicode_word = (unicodedata.normalize('NFKD', word).
#             encode('ascii', 'ignore'))
#         return filter(str.isalpha, non_unicode_word).lower()

if __name__ == '__main__':
    #source_file = sys.argv[1]
    source_file = 'Data/SampleFinal.pdf'
    pdf_result = pdf_parser(source_file)
    print pdf_result

# from here, you can do a smart analysis using nearest neighbor
# or just base it on if then
# then suggest the result, then whether or not you want to move it
# if yes, then use: shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")