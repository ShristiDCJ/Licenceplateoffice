# Deploying to Render

## Prerequisites
- Render account (https://render.com)
- GitHub repository with your code
- No CLI required - deploy directly from dashboard

## Quick Start

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Connect to Render
- Go to https://render.com
- Sign in with GitHub (or create account)
- Click "New +" → "Web Service"
- Select your repository
- Render auto-detects Python and uses `render.yaml` config

### 3. Configure & Deploy
- **Name**: licence-plate-office (customize as needed)
- **Runtime**: Python (auto-detected)
- **Build Command**: Listed in render.yaml
- **Start Command**: Listed in render.yaml
- Click "Create Web Service"

That's it! Your app deploys automatically. You'll get a URL like `https://<service-name>.onrender.com`

## Configuration

The `render.yaml` file contains:
- **Runtime**: Python 3.10
- **Build**: Installs dependencies from `requirements.txt`
- **Start**: Runs via Gunicorn (production WSGI server)

## Important Notes

### Database (SQLite)
- SQLite works on Render but is **not persistent**
- With free tier, the database resets when the service restarts
- For production/persistent data, use Render's PostgreSQL:
  1. Add PostgreSQL from Render dashboard
  2. Update `app.py` to use the `DATABASE_URL` environment variable
  3. Here's a quick migration guide below

### Performance
- Free tier has limited resources (0.5 CPU, 512MB RAM)
- Paid plans available for better performance
- Your app will auto-deploy when you push to GitHub (if connected)

## Environment Variables

Add via Render Dashboard (Settings → Environment):
```
DATABASE_URL=your_database_url (if using PostgreSQL)
FLASK_ENV=production
```

Currently no environment variables are required.

## Auto-Deploy from GitHub

1. Your repo is connected during setup
2. Every push to `main` branch auto-deploys
3. View build logs in Render dashboard

## Verification

After deployment:
1. Render provides a public URL
2. Visit the URL to test your app
3. Check "Logs" tab if issues occur
4. View metrics and restart service if needed

## Upgrading to PostgreSQL (Persistent Database)

For production with persistent data:

1. **Create PostgreSQL instance**:
   - Render Dashboard → "New +" → "PostgreSQL"
   - Name: licence-plate-office-db
   - Region: Same as your web service
   - Create

2. **Install psycopg2**:
   ```bash
   pip install psycopg2-binary
   ```
   Add to `requirements.txt`

3. **Update app.py** to use PostgreSQL instead of SQLite

4. **Redeploy**: Push changes to GitHub, Render auto-deploys

## Monitoring & Logs

- **Logs**: Render Dashboard → Logs tab
- **Metrics**: Dashboard → Metrics (CPU, Memory, Network)
- **Health**: Dashboard shows service status
- **Restart Service**: Use dashboard button if needed

## Troubleshooting

**Build Failed**
- Check build logs in dashboard
- Verify `requirements.txt` syntax
- Ensure your repo is connected properly

**App won't start**
- Check runtime logs for errors
- Verify `render.yaml` syntax
- Ensure port is correct (PORT env var)

**Database Issues**
- Check if using free tier (data isn't persistent)
- For persistent needs, add PostgreSQL
- View database logs in separate dashboard tab
   ```
3. **Update app.py** to use PostgreSQL instead of SQLite
4. **Set DATABASE_URL** environment variable in Vercel
5. **Re-deploy**

Example PostgreSQL connection:
```python
import os
import psycopg2

DB_URL = os.environ.get('DATABASE_URL')
```

---

For more details, visit:
- Vercel Python Docs: https://vercel.com/docs/concepts/functions/serverless-functions/python
- Flask on Vercel: https://vercel.com/guides/deploying-flask-with-vercel
