# Importing Pdf writer
from PyPDF2 import PdfMerger
import os

files_d = []
files = os.listdir()

for entry in files:
    if entry.endswith('.pdf'):
        files_d.append(entry)
        print(f"The detected pdf's are {entry}")

# Assigning the PdfMerger
merger = PdfMerger()

# Creating loop to merge pdfs
# Also specify the name of the merged pdf
merged_name = input("Enter the name for your combined pdf: ")

if (".pdf") in merged_name:
    merged_name = merged_name.replace(".pdf", "")

arg = input("TYPE Y TO CONTINUE: ")

if arg == "y" or arg == "Y":
    for pdf in files_d:
        merger.append(pdf)

    # Write the merged PDF to the specified name
    with open(f"{merged_name}.pdf", "wb") as output_pdf:
        merger.write(output_pdf)

    print("PDFs merged successfully.")

else:
    exit()

