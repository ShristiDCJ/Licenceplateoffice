from flask import Flask, render_template, jsonify, request
import sqlite3
import os

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

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
