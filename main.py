# project: fake invoice detector using computer vision

# considering original invoice format from this dataset:
# https://www.kaggle.com/datasets/osamahosamabdellatif/high-quality-invoice-images-for-ocr

# run: python app.py
# go to: http://127.0.0.1:5000/

from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mahaq\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def check_invoice(image_path):
    image = Image.open(image_path).convert("L")
    text = pytesseract.image_to_string(image)

    print(text)

    # extract fields using regex
    invoice_no = re.search(r'Invoice\s*no[:\-]?\s*(\d+)', text, re.IGNORECASE)
    date = re.search(r'Date\s*.*[:\-]?\s*(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
    if not date:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if line.strip().lower() == "total":
                if i + 2 < len(lines):
                    match = re.search(r'(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
                    if match:
                        date = match
                break
    iban = re.search(r'IBAN[:\-]?\s*([A-Z0-9]+)', text, re.IGNORECASE)
    client_tax = re.findall(r'Tax\s*Id[:\-]?\s*(\d{3}-\d{2}-\d{4})', text)
    if len(client_tax) >= 2:
        seller_tax_id, client_tax_id = client_tax[0], client_tax[1]
    else:
        seller_tax_id = client_tax_id = "not found"

    # outputs
    print("invoice no:", invoice_no.group(1) if invoice_no else "not found")
    print("date of issue:", date.group(1) if date else "not found")
    print("seller tax id:", seller_tax_id)
    print("client tax id:", client_tax_id)
    print("iban:", iban.group(1) if iban else "not found")

    fields = {
        "Invoice No": invoice_no.group(1) if invoice_no else "not found",
        "Date of Issue": date.group(1) if date else "not found",
        "Seller Tax ID": seller_tax_id,
        "Client Tax ID": client_tax_id,
        "IBAN": iban.group(1) if iban else "not found",
    }

    if not invoice_no or not date or not iban or seller_tax_id == "not found" or client_tax_id == "not found":
        result = "Fake Invoice"
    else:
        result = "Original Invoice"

    return fields, result
