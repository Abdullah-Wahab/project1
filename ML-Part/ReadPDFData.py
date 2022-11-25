import PyPDF2

file = open("sample.pdf", "rb")
reader = PyPDF2.PdfFileReader(file)
page1 = reader.getPage(0)
extraction = page1.extractText()

# Printing the full page 1
print(extraction)

# Printing the number of pages
print(reader.numPages)

# Printing the Document Information
print(reader.documentInfo)


# Extracting and then writing in text file
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(extraction)

# To Check if a value exist in the file or not
assert "ACORD" in extraction

