# Fake Invoice Detector

A simple web app to detect fake invoices using Tesseract OCR, SHA256 hashing, and layout template matching through OpenCV.

---

## Features

- Upload and analyze invoices to determine if they're fake or original.
- Add known original invoices to a safe-list using SHA256 of OCR'd text.
- Template-based layout matching using OpenCV.
- Field extraction using regular expressions (Invoice No, Date, Tax IDs, IBAN).
- Flask-powered web interface.

---

## Sample Dataset

Based on invoice format from:  
🔗 [High Quality Invoice Images for OCR - Kaggle](https://www.kaggle.com/datasets/osamahosamabdellatif/high-quality-invoice-images-for-ocr)

---

## Installation

```bash
# Clone the repo
git clone https://github.com/mahaqj/Fake-Invoice-Detector.git
cd Invoice-Detector

python -m venv venv
venv\Scripts\activate # on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## How It Works

1. **Analyze Invoice**:
    - Extracts text from uploaded invoice using Tesseract OCR
    - Computes SHA256 hash of the text
    - Checks if this hash matches any known original invoice's hash and further uses OpenCV template matching and field presence to classify the invoice label

2. **Add Original Invoice**:
    - User uploads an original invoice image
    - The SHA256 hash of its OCR text is stored in `original_hashes.txt`

---

## How to Run

Make sure Tesseract OCR is installed and set the correct path in `main.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mahaq\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
```

Then on the terminal:

```bash
# 1. Install dependencies
pip install flask pillow pytesseract opencv-python

# 2. Make sure Tesseract-OCR is installed and added to PATH

# 3. Run the Flask app
python app.py
```

---

## Example Results



---

## 📌 Notes

- Template matching threshold is set to `0.4`.
- SHA256 is used to verify exact matches to known originals.

---