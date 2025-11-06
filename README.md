# python_ASSIGNMENT-2
This is a simple Django rest api which is fetch joke and store it in db, and we can fetch joke from it.

#  Django Joke API Project

##  Overview

This Django project integrates with a public **Joke API** to fetch 100 jokes, store them in a local database, and expose endpoints to view or retrieve jokes via REST APIs. It demonstrates Django’s ORM capabilities, API integration, and RESTFUL view design.

---

##  Features

* Fetch 100 random jokes from an external Joke API
* Store jokes in the database using Django ORM
* API endpoint to display 1 jokes
* Optional endpoint to fetch  jokes by limit
* Simple, modular Django architecture (views, models, serializers)

---

## Project Structure

```
joke_project/
│
├── joke_app/                     # Main application
│   ├── models.py                 # Joke model
│   ├── views.py                  # Fetch + display logic
│   ├── urls.py                   # API routes
│   └── serializers.py            # (If using DRF)
│
├── joke_project/
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Root routing

│
├── manage.py
├── requirements.txt
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-joke-api.git
cd django-joke-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---



###  1. Run the development server

```bash
python manage.py runserver
```

###  2. Fetch and store jokes

Open your browser or use curl:

```bash
GET http://127.0.0.1:8000/api/Fetch/
```

This will:

* Call the external Joke API
* Fetch 100 jokes
* Store them in the database

###  3. View stored jokes

```bash
GET http://127.0.0.1:8000/api/get_jokes/
```

Returns 1 stored jokes in JSON format.


---

##  API Endpoints Summary

| Endpoint           | Method | Description                   |
|--------------------| ------ |-------------------------------|
| `/api/Fetch//`     | GET    | Fetch 100 jokes from external API and store in DB |
| `/api/get_jokes/`  | GET    | Retrieve 1 jokes from DB      |
| `/api/get_jokes/?<br/>?limit=100` | GET    | Retrieve 100 jokes from DB    |
---

##  Requirements

* Python 3.9+
* Django 4.x+
* requests (for external API calls)
* djangorestframework (for APIs)


