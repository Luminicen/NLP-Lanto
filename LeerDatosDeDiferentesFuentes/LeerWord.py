#pip install python-docx
from docx import Document
#Creating a word file object
doc = open("ejemplo.docx","rb")
#creating word reader object
document = Document(doc)
# create an empty string and call this document. This document variable store each paragraph in the Word document.We then create a for loop that goes through each paragraph in the Word document and appends the paragraph.
docu=""
for para in document.paragraphs:
 docu += para.text
#to see the output call docu
print(docu)