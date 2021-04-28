import PyPDF2
import os 
import re

data_path = os.path.dirname(__file__) + "/data/210428_nsw_epidemiology_reports/"

# strings_to_check = ["Country of acquisition"]
strings_to_check = ["Top 10 countries of acquisition"]
# Top 10 countries of acquisition
count = 1

pdf_writer = PyPDF2.PdfFileWriter()
for file in os.listdir(data_path):
    obj = PyPDF2.PdfFileReader(f"{data_path }{file}")
    num_pages = obj.getNumPages()
 

    for string in strings_to_check:
        # print(f"Checking: {string}\n")
        # print(file)
        print(count)

        for i in range(0, num_pages):
            PageObj = obj.getPage(i)
            Text = PageObj.extractText().lower()
            if re.search(string.lower(),Text):
                print("Pattern Found on Page: " + str(i))
                print(file)
                final_page = obj.getPage(i)
                pdf_writer.addPage(final_page)
        count +=1

new_data_path = os.path.dirname(__file__) + "/data/"
with open(f"{new_data_path}countries_of.pdf", "wb") as f:
    pdf_writer.write(f)