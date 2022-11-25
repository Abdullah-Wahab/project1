import PyPDF2

file = open("handwritten-1.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)

print(reader.numPages)


page1 = reader.getPage(7)
extraction = page1.extractText()

print(extraction)
