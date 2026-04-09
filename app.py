from flask import Flask, render_template, jsonify, request
import sqlite3
import os
import easyocr
import base64
from io import BytesIO
from PIL import Image
import numpy as np

app = Flask(__name__, template_folder='templates')
DB_PATH = os.path.join(os.path.dirname(__file__), 'hello_world.db')

def init_db():
    """Initialize the database with sample data"""
    try:
        if not os.path.exists(DB_PATH):
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL
                )
            ''')
            
            cursor.execute("INSERT INTO messages (text) VALUES ('Hello World from Database!')")
            conn.commit()
            conn.close()
            print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")

# Initialize database on app startup
init_db()

# Initialize EasyOCR reader (loads model on startup)
try:
    reader = easyocr.Reader(['en'])
    print("EasyOCR reader initialized successfully")
except Exception as e:
    print(f"EasyOCR initialization error: {e}")
    reader = None

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/ocr', methods=['POST'])
def perform_ocr():
    """Perform OCR on uploaded image"""
    try:
        if 'image' not in request.json:
            return jsonify({'error': 'No image provided'}), 400
        
        # Decode base64 image
        image_data = request.json['image']
        if ',' in image_data:
            image_data = image_data.split(',')[1]
        
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        image_array = np.array(image)
        
        if reader is None:
            return jsonify({'error': 'OCR model not initialized'}), 500
        
        # Perform OCR
        results = reader.readtext(image_array, detail=0)
        detected_text = ' '.join(results)
        
        # Clean text
        cleaned_text = detected_text.replace('\n', ' ').strip()
        cleaned_text = ''.join(c for c in cleaned_text if c.isalnum() or c.isspace())
        cleaned_text = ' '.join(cleaned_text.split())
        
        return jsonify({
            'text': cleaned_text,
            'success': True
        })
    
    except Exception as e:
        print(f"OCR error: {e}")
        return jsonify({'error': str(e), 'success': False}), 500

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
