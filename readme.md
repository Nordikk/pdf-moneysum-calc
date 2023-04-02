# 📝 PDF MoneySum Calculator

This Python program reads money amounts from PDF files and calculates the total sum of all money amounts. It is useful when you have invoices in PDF format and need to quickly calculate the total sum.

## 🚀 Getting Started

1. Clone the repository: `git clone https://github.com/<username>/<repository>.git`
2. Navigate to the directory: `cd <repository>/pdf-money-reader`
3. Install the required Python libraries: `pip install PyPDF2`
4. Place the PDF files you want to read in the `pdf` directory
5. Run the program: `python moneyreader.py`

## 📁 Directory Structure

The program assumes that all PDF files are located in the `pdf` subdirectory and have the `.pdf` extension.

## 📜 Features

The program reads the money amount from each PDF file that follows the word "Gesamtpreis" and calculates the total sum of all money amounts. The result is rounded to two decimal places and outputted to the console.

## 📝 Notes

- The program only reads the money amount that follows the word "Gesamtpreis". If the money amount is labeled differently, the regular expression needs to be adjusted accordingly.
- The program assumes that all money amounts are formatted as "1,234.56 €" or "1,234.56 EUR". If the money amounts are formatted differently, the code needs to be adjusted.


