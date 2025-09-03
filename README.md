# Chat Me 🗨️

A Django-based chat application with Tailwind CSS for styling.  
This project demonstrates a real-time chat interface with a modern, responsive design.

---

## Features

- Django backend for handling chat logic
- Tailwind CSS for responsive UI
- Modular app structure (`chat_me/khuluma`)
- Ready for extension with WebSockets or REST APIs

---

## Project Structure

```bash
    chat_me/
├─ khuluma/
│ ├─ migrations/
│ ├─ templates/
│ │ └─ khuluma/
│ │ └─ chat.html
│ ├─ static/
│ ├─ views.py
│ ├─ urls.py
│ └─ models.py
├─ chat_me/
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
├─ manage.py
├─ package.json
├─ tailwind.config.js
└─ postcss.config.js
```


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd chat_me
```

2. Create a Python virtual environment
```bash
python -m venv backend_env
```
3. Install Python dependencies
```bash
pip install -r requirements.txt
```
4. Install Node.js dependencies
```bash
npm install
```
5. Build Tailwind CSS
```bash
npm run watch:css
```

This will compile static/css/main.css to static/output.css and watch for changes.

6. Run Django migrations
```bash
python manage.py migrate
```
7. Start the server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

> [!Notes]
> Templates must be placed under templates/<app_name>/.

For example: khuluma/templates/khuluma/chat.html

Tailwind CLI must be installed locally and referenced in package.json scripts.

Make sure APP_DIRS = True in settings.py.

# License

This project is open-source and available under the MIT License
.

# Author

- Simanga Mchunu Developer