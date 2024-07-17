import PyPDF2
import torch
from sentence_transformers import SentenceTransformer, util

# Load a lightweight model
model = SentenceTransformer('all-mpnet-base-v2')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)  # Use len(pdf_reader.pages) for PyPDF2 >= 3.0.0

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]  # Use pdf_reader.pages[index] for PyPDF2 >= 3.0.0
            text += page.extract_text()

    return text

def find_information(text, query):
    sentences = text.split('\n')
    print(sentences)
    embeddings = model.encode(sentences, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    best_idx = torch.argmax(scores).item()
    return sentences[best_idx]

def extract_invoice_details(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    
    seller_name_query = "return dispatch date"
    total_amount_query = "returnt maximum total amount for Deepshakti Oil"
    total_nos_query = "returnt Total ₹"
    
    seller_name = find_information(text, seller_name_query)
    total_amount = find_information(text, total_amount_query)
    total_nos = find_information(text, total_nos_query)
    
    return seller_name, total_amount, total_nos

# Path to your PDF file
pdf_path = '121.pdf'

# Extract details
seller_name, total_amount, total_nos = extract_invoice_details(pdf_path)

print("Seller Name:", seller_name)
print("Total Amount:", total_amount)
print("Total Nos:", total_nos)
