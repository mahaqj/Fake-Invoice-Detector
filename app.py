from flask import Flask, render_template, request
from main import check_invoice
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    fields = {}
    if request.method == "POST":
        file = request.files['invoice']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            fields, result = check_invoice(filepath) # run ocr
    return render_template("index.html", fields=fields, result=result)

if __name__ == "__main__":
    app.run(debug=True)
