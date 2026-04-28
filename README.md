# Licence Plate Office

## Overview
A full-stack web application for capturing and decoding vehicle number plates using OCR (Optical Character Recognition). The app provides a clean, responsive interface for camera-based number plate scanning that works on both mobile and desktop devices.

## Tech Stack
- **Backend**: Python 3.x with Flask
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **OCR Engine**: Tesseract.js (client-side processing)
- **Database**: SQLite (initialized, currently unused by frontend)
- **Production Server**: Gunicorn

## Project Structure
```
├── app.py                 # Flask application (backend)
├── templates/
│   └── index.html         # Frontend UI with camera & OCR
├── requirements.txt       # Python dependencies
├── render.yaml            # Render deployment configuration
├── vercel.json            # Vercel deployment configuration
├── DEPLOYMENT.md          # Detailed deployment instructions
├── hello_world.db         # SQLite database (auto-created)
└── .gitignore             # Git ignore rules
```

## Features
- **Camera Capture**: Real-time camera access with environment-facing camera preference
- **OCR Recognition**: Uses Tesseract.js to extract text from captured images
- **Instant Results**: Displays detected number plate text immediately after capture
- **Mobile Responsive**: Optimized layout for both mobile and desktop screens
- **Multiple Deployment Options**: Ready to deploy on Render or Vercel

## Setup & Running Locally

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

The app will automatically initialize the SQLite database on first run.

## How It Works

1. **Frontend**: The browser loads the HTML page served by Flask
2. **Camera Access**: Click "Start Camera" to access the device camera
3. **Capture**: Click "Capture" to take a photo of the number plate
4. **OCR Processing**: Tesseract.js processes the image client-side and extracts text
5. **Display**: The detected text is displayed along with the captured image

> **Note**: All OCR processing happens in the browser using Tesseract.js. No images are sent to the server.

## Deployment

This project is ready to deploy on multiple platforms:

- **Render**: Uses `render.yaml` configuration with Gunicorn
- **Vercel**: Uses `vercel.json` configuration for serverless deployment

See [`DEPLOYMENT.md`](DEPLOYMENT.md) for step-by-step deployment instructions for both platforms.

## API Endpoints

- `GET /` - Serves the main application page (`index.html`)

## Requirements

- Python 3.10+
- Modern web browser with camera support
- HTTPS (required for camera access on most mobile browsers when not on localhost)

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.3.3 | Web framework |
| Werkzeug | 2.3.7 | WSGI utilities |
| Pillow | >=11.0.0 | Image processing library |
| gunicorn | 21.2.0 | Production WSGI server |

## Notes

- The backend initializes a SQLite database (`hello_world.db`) on startup, but the current frontend operates entirely client-side and does not interact with it
- Camera access requires a secure context (HTTPS) or localhost on most modern browsers
- For persistent data storage in production, consider migrating from SQLite to PostgreSQL (see `DEPLOYMENT.md` for guidance)

---
**License**: MIT

