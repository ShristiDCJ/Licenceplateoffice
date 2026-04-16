# Full Stack Licence Plate Reader App - README

## Overview
This is a full-stack "Hello World" application demonstrating:
- **Backend**: Python with Flask
- **Frontend**: HTML/CSS/JavaScript
- **Database**: SQLite (local database)

## Project Structure
```
├── app.py                 # Flask application (backend)
├── templates/
│   └── index.html        # Frontend HTML/CSS/JavaScript
├── hello_world.db        # SQLite database (auto-created)
└── requirements.txt      # Python dependencies
```

## Setup & Running

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access the App
Open your browser and navigate to:
```
http://localhost:5000
```

## Features
- **Home Page**: Displays a greeting message from the database
- **Refresh Button**: Fetches the latest message from the database via API
- **Database Integration**: Uses SQLite to store and retrieve messages
- **Auto-initialization**: Database is automatically created on first run

## API Endpoints
- `GET /` - Main page (renders HTML with message)
- `GET /api/message` - JSON endpoint returning message from database

## How It Works
1. When the app starts, it initializes a SQLite database with a `messages` table
2. The initial message "Hello World from Database!" is inserted
3. The Flask backend serves the HTML frontend
4. The frontend makes API calls to fetch messages from the database
5. The "Refresh Message" button updates the message dynamically

## Customization
To change the initial message, edit `app.py` and modify the INSERT statement in the `init_db()` function.

---
**Tech Stack**: Python 3.x + Flask + SQLite + HTML5/CSS3/JavaScript
