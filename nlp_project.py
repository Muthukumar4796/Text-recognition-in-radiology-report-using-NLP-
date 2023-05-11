import PyPDF2
import warnings

# Open the PDF file in read-binary mode
pdf_file = open('1.2.826.1.3680043.9.5282.150415.2352.16502352212057.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

num_pages = len(pdf_reader.pages)
text = ""

for page_number in range(num_pages):
    page = pdf_reader.pages[page_number]
    page_text = page.extract_text()
    text += page_text
# print(text)
# print(type(text))

import re

# text = "Name MR.JITENDRA BHUPTANI 383669 Patient ID AS_BOR_CT_2746  Accession No 164_02746_212057 Age/Gender 80Y / Male  Referred By Dr.ANAND S. SHENAI MS Date 3-Oct-2021"

name_regex = r"Name\s+([A-Z\. ]+)"
patient_id_regex = r"Patient\s+ID\s+([\w-]+)"
accession_no_regex = r"Accession\s+No\s+([\d_]+)"
age_gender_regex = r"Age\/Gender\s+([\d]+[A-Za-z]*)\s+\/\s+([A-Za-z]+)"
date_regex = r"Date\s+(\d+-[A-Za-z]{3}-\d+)"

name = re.search(name_regex, text).group(1)
patient_id = re.search(patient_id_regex, text).group(1)
accession_no = re.search(accession_no_regex, text).group(1)
age, gender = re.search(age_gender_regex, text).groups()
date = re.search(date_regex, text).group(1)

print(f"Name: {name}")
print(f"Patient ID: {patient_id}")
print(f"Accession No: {accession_no}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Date: {date}")





