import os
import PyPDF2
import re

pdf_folder = 'pdf/'
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

total_money_amount = 0

for pdf_file in pdf_files:
    with open(os.path.join(pdf_folder, pdf_file), 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)
        content = ''
        for page in range(len(pdf_reader.pages)):
            content += pdf_reader.pages[page].extract_text()

    money_regex = r'(?:Gesamt|Zwischen)summe.*?(\d{1,3}(?:\.\d{3})*(?:,\d{2})?\s*(?:€|EUR))'
    match = re.search(money_regex, content, re.DOTALL)

    if match:
        money_amount = match.group(1)
        money_amount = money_amount.replace('.', '').replace(',', '.').replace('EUR', '').replace('€', '').strip()
        total_money_amount += float(money_amount)

total_money_amount = round(total_money_amount, 2)

print("Total Amount:", total_money_amount)
