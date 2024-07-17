import PyPDF2
from sentence_transformers import SentenceTransformer

# Load a lightweight model
model = SentenceTransformer('all-mpnet-base-v2')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            extracted_page_text = page.extract_text()
            text += extracted_page_text.replace('\t', '    ')  # Replace tabs with 4 spaces

        return text

def main():
    pdf_path = '121.pdf'  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Compute embeddings
    embeddings = model.encode(extracted_text)
    
    # Print embeddings or further process them
    print("Embeddings:")
    print("Text and Embeddings:")
    for text, emb in zip(extracted_text.splitlines(), embeddings):
        print(f"Text: {text}")
        print(f"Embedding: {emb}")
        print()  # Empty line for readability

if __name__ == "__main__":
    main()
