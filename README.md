# 🛩️ Alpha Jet Sortie Manager API

**Squadron Sortie Management System**

A robust Django REST Framework API designed to manage aircraft maintenance, pilot readiness, and mission scheduling with strict validation logic.

## 🚀 Live Demo

**Base URL:** `http://orionaji.pythonanywhere.com/api/v1/`

**Interactive Docs:** `http://orionaji.pythonanywhere.com/api/docs/`

---

## 🛠️ Key Features

* **Fleet Readiness Tracking:** Real-time status of Alpha Jet aircraft (Ready, In Maintenance, Grounded).
* **Pilot Management:** Tracking ranks, callsigns, and flight eligibility.
* **Mission Validation (Criterion 8):** Automatic blocking of sorties if an aircraft is grounded or a pilot is not rested.
* **Security (Criterion 5):** Dual-layer authentication using **Session Cookies** for web users and **Auth Tokens** for external integrations.
* **Interactive Documentation:** Full Swagger UI integration for live API testing.

---

## 🔐 Authentication & Access

This API is protected. To access the data, you must first create an account.

### 1. Web Registration

Visit `/accounts/signup/` to create a pilot profile. Once logged in, you can browse the API via the web interface.

### 2. Token Authentication (for Postman/cURL)

To use the API programmatically, obtain a secret token:
**Endpoint:** `POST /api-token-auth/`
**Payload:**

```json
{
    "username": "your_username",
    "password": "your_password"
}

```

**Usage:** Include the token in your request headers:
`Authorization: Token <your_token_string>`

---

## 📊 API Endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/v1/aircraft/` | GET/POST | View fleet or add new aircraft. |
| `/api/v1/aircraft/readiness_report/` | GET | **Custom Action:** View summary of fleet status. |
| `/api/v1/pilots/` | GET/POST | Manage pilot directory and ranks. |
| `/api/v1/sorties/` | GET/POST | Schedule missions (Validation enforced). |
| `/api/docs/` | GET | **Swagger UI** documentation. |

---

## 🛡️ Business Logic & Validation

The system enforces squadron safety protocols during the `POST /api/v1/sorties/` process:

1. **Aircraft Check:** If an aircraft status is "In Maintenance" or "Grounded", the mission is blocked with a `400 Bad Request`.
2. **Audit Logging:** Every blocked attempt is recorded in the `squadron_errors.log` for safety reviews.

---

## ⚙️ Tech Stack

* **Core:** Django 5.1 / Python 3.13
* **API Framework:** Django REST Framework (DRF)
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Documentation:** drf-spectacular (Swagger/OpenAPI 3.0)
* **Filtering:** django-filter

---

## 👨‍💻 Installation (Local Setup)

1. Clone the repo: `git clone <repo-url>`
2. Create virtualenv: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

---
