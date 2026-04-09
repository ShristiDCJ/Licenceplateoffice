from flask import Flask, render_template, jsonify, request
import sqlite3
import os
import easyocr
from PIL import Image
import io
import base64

app = Flask(__name__, template_folder='templates')
DB_PATH = os.path.join(os.path.dirname(__file__), 'hello_world.db')

# Initialize EasyOCR reader (loads on first use)
ocr_reader = None

def get_ocr_reader():
    """Lazy load OCR reader to avoid memory issues"""
    global ocr_reader
    if ocr_reader is None:
        ocr_reader = easyocr.Reader(['en'], gpu=False)
    return ocr_reader

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

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/ocr', methods=['POST'])
def process_ocr():
    """Process image with EasyOCR and extract text"""
    try:
        # Get image from request
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        image_file = request.files['image']
        
        # Read image
        img = Image.open(image_file.stream)
        
        # Perform OCR using EasyOCR
        reader = get_ocr_reader()
        results = reader.readtext(img)
        
        # Extract text from results
        text_lines = []
        for (bbox, text, confidence) in results:
            if confidence > 0.3:  # Filter low confidence results
                text_lines.append(text)
        
        # Clean extracted text
        full_text = ' '.join(text_lines)
        cleaned_text = full_text.replace('\n', ' ').strip()
        cleaned_text = ''.join(c for c in cleaned_text if c.isalnum() or c.isspace()).strip()
        cleaned_text = ' '.join(cleaned_text.split())  # Remove extra spaces
        
        return jsonify({
            'success': True,
            'text': cleaned_text,
            'confidence': sum([conf for _, _, conf in results]) / len(results) if results else 0
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
