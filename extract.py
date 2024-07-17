import PyPDF2
import pandas as pd

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)  # Use len(reader.pages) for PyPDF2 >= 3.0.0

        all_text = []
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]  # Use reader.pages[index] for PyPDF2 >= 3.0.0
            all_text.append(page.extract_text())

        return all_text

def export_text_to_excel(all_text, excel_path):
    with pd.ExcelWriter(excel_path) as writer:
        for i, text in enumerate(all_text):
            df = pd.DataFrame({'Page': [i+1], 'Text': [text]})
            df.to_excel(writer, sheet_name=f'Page_{i+1}', index=False)

def read_pdf_to_excel(pdf_path, excel_path):
    all_text = extract_text_from_pdf(pdf_path)
    export_text_to_excel(all_text, excel_path)

# Example usage:
pdf_path = "121.pdf"
excel_path = "output_excel.xlsx"

read_pdf_to_excel(pdf_path, excel_path)

