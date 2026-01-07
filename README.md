# Flask + React Boilerplate

THIS IS A WORK IN PROGRESS

A minimal boilerplate for building a web app with a Flask backend and a React frontend.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Prerequisites

- Python (3.8+ recommended)
- pipenv (for backend)
- Node.js & npm (for frontend)
- Git (optional)

---

## Setup

### Backend

1. Open a terminal, then:

```bash
cd backend
pipenv install
pipenv shell
python main.py
```

The Flask server will start and auto-reload on code changes.

### Frontend

1. Open a new terminal, then:

```bash
cd frontend
npm install
npm start
```

The React dev server will start (hot reload enabled).

---

## Development Notes

- Edit `frontend/src/App.tsx` to see instant updates in the browser.
- Backend changes trigger Flask's auto-reloader.

---

## License

MIT
