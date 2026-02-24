from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from skintone import detect_skin_tone

# ✅ FIRST define Flask app
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ✅ AFTER that only routes
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        tone = detect_skin_tone(filepath)

        if tone == "Fair":
            suggestion = "Pastel Pink, Sky Blue, Lavender outfits will suit you."
        elif tone == "Medium":
            suggestion = "Mustard, Teal, Olive Green outfits will suit you."
        else:
            suggestion = "Royal Blue, Bright Yellow, White outfits will suit you."

        return render_template("index.html", tone=tone, suggestion=suggestion)

    return render_template("index.html", tone="Invalid", suggestion="Upload valid image")


if __name__ == "__main__":
    app.run(debug=True)