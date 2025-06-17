# Fake Invoice Detector

This is a simple web application that detects whether an invoice is **original or fake** using **Tesseract OCR** and comparing layout and **OpenCV**.

---

## How it Works

1. Extracts text from invoice images using **Tesseract OCR**
2. Uses **regular expressions** to extract key fields:
   - Invoice Number
   - Date of Issue
   - IBAN
   - Seller and Client Tax IDs
3. Classifies invoice as:
   - **Original** -> if layout matches and all fields are found
   - **Fake** -> if layout mismatches or key fields are missing

---

## Assumption

Correct format of invoice matches the images of invoices from https://www.kaggle.com/datasets/osamahosamabdellatif/high-quality-invoice-images-for-ocr

---

## How to Run

```bash
# 1. Install dependencies
pip install flask pillow pytesseract opencv-python

# 2. Make sure Tesseract-OCR is installed and added to PATH

# 3. Run the Flask app
python app.py
```

Then open:  
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Web App Usage Flow

1. Upload invoice image
2. App matches template, runs OCR and extracts fields
3. Result is shown:
   - Extracted fields
   - Invoice status (Original or Fake)

---

## Sample Results

Original Invoice Input:
![batch1-1003](https://github.com/user-attachments/assets/6f813408-e2a4-4a07-b38d-2ea5959a6692)
Output:
![Screenshot 2025-06-17 130524](https://github.com/user-attachments/assets/7045c56c-f30e-454e-9407-c9238c9618a6)

---

## Tech Stack

- **Image Processing**: OpenCV
- **Backend**: Python + Flask
- **OCR**: Tesseract (via pytesseract)
- **Frontend**: HTML + CSS

---
