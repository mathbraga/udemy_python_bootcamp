import PyPDF2
import csv
import re

f = open("src/find_the_link.csv", encoding="utf-8")
csv_file = csv.reader(f)
data = list(csv_file)

count = 0
link = ""
for n in data:
    link += n[count]
    count += 1
print(link)

f.close()
f = PyPDF2.PdfFileReader("src/Find_the_Phone_Number.pdf")

match = []
res = []
for page in range(f.getNumPages()):
    page_content = f.getPage(page)
    page_text = page_content.extractText()
    res = re.findall(r"\d{3}.\d{3}.\d{4}", page_text)
    if res:
        match.append(res)

print(match)
