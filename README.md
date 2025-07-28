# Budget Tracker App

This is a **simple (and IN PROGRESS) web-based Budget Tracking App** built with **FastAPI**, **Jinja2**, **SQLite**.

🔗 **Live App**: [https://budgetify-sw76.onrender.com/](https://budgetify-sw76.onrender.com/)  
🔗 **API DOCS**: [https://budgetify-sw76.onrender.com/docs](https://budgetify-sw76.onrender.com/docs)    

---

## Features

- Create budgets with starting amounts
-  Set spending limits
-  Add expenses per budget
-  Automatic calculation of remaining budget
-  Visual indicator for over/under budget

---

##  Getting Started Locally

### Prerequisites

- Python 3.11+
- SQLite (comes by default)
- `pip` for dependency management

### 1. Clone the repo

```bash
git clone https://github.com/your-username/budget-tracker.git
cd budget-tracker
```

### 2. Create a virtual environment & install dependencies

If using `venv`:

```bash
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Initialize the database

Run the database initialization script:

```bash
python3 src/db/init_db.py
```

This will create the required SQLite tables.

### 4. Run the server

```bash
uvicorn src.main:app --reload
```

Visit `http://localhost:8000` to use the app.

---

## Folder Structure

```
src/
├── api/            # Routes and schemas
├── db/             # Database models and init_db.py
├── models/         # Pydantic schemas
├── templates/      # Jinja2 HTML template
└── main.py         # FastAPI app entry point
```

---
