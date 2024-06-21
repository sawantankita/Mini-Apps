from pdf2docx import Converter
pdf_file='A4 Output.pdf'
docx_file='sampledoc.docx'
cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()