import PyPDF2

# Read the report text

# Open the PDF file in read-binary mode
pdf_file = open('1.2.826.1.3680043.9.5282.150415.2428.15502428212057.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)

num_pages = len(pdf_reader.pages)
text = ""

for page_number in range(num_pages):
    page = pdf_reader.pages[page_number]
    page_text = page.extract_text()
    text += page_text
print(text)

# Extract patient information
def extract_patient_info(text):
    import re
    patient_id = re.search(r'Patient ID\s+(\S+)', text).group(1)
    accession_no = re.search(r'Accession No\s+(\S+)', text).group(1)
    age_gender = re.search(r'Age/Gender\s+(.+)', text).group(1)
    referred_by = re.search(r'Referred By\s+(.+)', text).group(1)
    date = re.search(r'Date\s+(\S+)', text).group(1)
    return patient_id, accession_no, age_gender, referred_by, date

patient_id, accession_no, age_gender, referred_by, date = extract_patient_info(text)

# Extract report information
def extract_report_info(text):
    import re
    technique = re.search(r'TECHNIQUE:\s+(.+)', text).group(1)
    observation = re.search(r'OBSERVATION:\s+(.+?)IMPRESSION', text, re.DOTALL).group(1).strip()
    impression = re.search(r'IMPRESSION:\s+(.+)', text).group(1)
    return technique, observation, impression

technique, observation, impression = extract_report_info(text)

# Print extracted information
print("Patient ID:", patient_id)
print("Accession No:", accession_no)
print("Age/Gender:", age_gender)
print("Referred By:", referred_by)
print("Date:", date)
# print("Technique:", technique)
# print("Observation:", observation)
print("Impression:", impression)


