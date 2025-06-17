from flask import Flask, render_template, request
from main import check_invoice, extract_text_fields
import os
import hashlib

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# @app.route("/", methods=["GET", "POST"])
# def index():
#     result = None
#     fields = {}
#     if request.method == "POST":
#         file = request.files['invoice']
#         if file:
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filepath)
#             fields, result = check_invoice(filepath) # run ocr
#     return render_template("index.html", fields=fields, result=result)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    fields = {}
    if request.method == "POST":
        file = request.files.get('invoice')
        if file and file.filename:  # <--- check that a file is selected
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            fields, result = check_invoice(filepath)
        else:
            result = "Please select a file before submitting."
    return render_template("index.html", fields=fields, result=result)

@app.route("/upload_original", methods=["POST"])
def upload_original():
    file = request.files['original_invoice']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'original', file.filename)
        file.save(filepath)

        # generate sha256 from OCR text
        fields, text = extract_text_fields(filepath)
        sha256 = hashlib.sha256(text.encode()).hexdigest()

        # append hash to known originals file
        with open("original_hashes.txt", "a") as f:
            f.write(sha256 + "\n")

    return "Original invoice added successfully! <a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
