import os
import PyPDF2
folder_path = "D:\\3rd-year-1st-semster\\Algorithms\\lectures"
files = os.listdir(folder_path)
os.chdir(folder_path)
print(files)
# importing required modules
pages = 0
for pdf in files:
    # creating a pdf file object
    pdfFileObj = open(pdf, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    print("pdf name: ", pdf, " page_count: ", pdfReader.numPages)
    pages += pdfReader.numPages
    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    print(pageObj.extractText())
    # closing the pdf file object
    pdfFileObj.close()
print("total number of pages is ", pages)
