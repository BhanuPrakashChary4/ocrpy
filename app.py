from flask import Flask, render_template, request, redirect, url_for
import pytesseract
from PIL import Image
import os

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'  # Folder to store uploaded images

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def ocr_image(image_path):
    """Extract text from the image using Tesseract OCR."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error processing image: {e}"

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    """Handle image uploads and perform OCR."""
    uploaded_files = request.files.getlist("images")  # Get multiple image files
    if not uploaded_files:
        return redirect(url_for('index'))

    ocr_results = {}
    for file in uploaded_files:
        if file.filename != '':
            # Save the file to the upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Perform OCR on the saved image
            text = ocr_image(file_path)

            # Store the result
            ocr_results[file.filename] = text

    # Render results page
    return render_template('results.html', ocr_results=ocr_results)

if __name__ == "__main__":
    app.run(debug=True)
