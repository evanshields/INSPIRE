import pdfplumber
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

pdfs = [
    "Eastview DSCR Guidelines_v7.2.pdf",
    "Archwest RTL Guidelines.pdf",
    "Eastview_RTL_Guidelines_v4_1.pdf",
    "1. Archwest DSCR Guidelines_7.9.25_V1.8.pdf",
    "EV GUC Guidelines_v1.0.pdf",
    "Churchill DSCR Guidelines - 8.8.2023 5.pdf",
    "Churchill RTL UPG - 06.2023_vf.pdf",
    "RTL Program Guidelines (07.09.2025) - CLEAN 1.pdf",
    "EV DSCR S Matrix_12.29.25.pdf"
]

for pdf_file in pdfs:
    pdf_path = os.path.join(script_dir, pdf_file)
    
    if not os.path.exists(pdf_path):
        print(f"Warning: File not found - {pdf_file}")
        continue
    
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"
        
        output_file = os.path.join(script_dir, pdf_file.replace('.pdf', '.txt'))
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Extracted: {pdf_file} -> {os.path.basename(output_file)}")

print("\nDone! All PDFs have been extracted to text files.")

