import PyPDF2
from PyPDF2 import PdfReader
#Creating a pdf file object
pdf = open("ejemplo.pdf","rb")
#creating pdf reader object
pdf_reader = PyPDF2.PdfReader(pdf)
#checking number of pages in a pdf file
print("Cantidad de paginas: ",len(pdf_reader.pages))
print("----------------------------- Pagina 0 -------------------------------")
#creating a page object
page = pdf_reader.pages[0]
#finally extracting text from the page
print(page.extract_text())
#closing the pdf file
pdf.close()