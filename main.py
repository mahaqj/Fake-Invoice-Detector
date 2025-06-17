# project: fake invoice detector using computer vision

from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\mahaq\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# image to grayscale to string
image = Image.open("C:\\Users\\mahaq\\Desktop\\fakeinvoice.jpg")
grayscale_image = image.convert("L")
grayscale_image.save("C:\\Users\\mahaq\\Documents\\VS Code Projects\\Invoice-Detector\\grayscale_image.jpg")
text = pytesseract.image_to_string(Image.open("grayscale_image.jpg"))
print(text)

# extract fields using regex
invoice_no = re.search(r'Invoice\s*no[:\-]?\s*(\d+)', text, re.IGNORECASE)
date = re.search(r'Date\s*of\s*issue[:\-]?\s*(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
iban = re.search(r'IBAN[:\-]?\s*([A-Z0-9]+)', text, re.IGNORECASE)
seller_tax = re.search(r'Tax\s*Id[:\-]?\s*(\d{3}-\d{2}-\d{4})', text)
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

if not invoice_no or not date or not iban or seller_tax == "not found" or client_tax == "not found":
    print("\nfake invoice")
else:
    print("\noriginal invoice")