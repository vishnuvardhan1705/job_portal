# Job Portal Backend (Django + DRF)

A production-ready **Job Portal Backend API** built using **Django, Django REST Framework, JWT authentication, and PostgreSQL**.

---

## 🚀 Features

### 🔐 Authentication & Authorization

* Custom User Model
* Role-based users: **Recruiter / Job Seeker**
* JWT Authentication (Login / Refresh)
* Secure password handling

### 👔 Recruiter Module

* Recruiter profile management
* Create, update, delete job postings
* View applicants for posted jobs

### 🧑‍💼 Job Seeker Module

* Job seeker profile
* View all available jobs
* Apply to jobs
* Track applied jobs

### 📄 Job Management

* Job CRUD APIs
* Job applications with status tracking
* Relational models (User ↔ Jobs ↔ Applications)

### ⚙️ Production Ready

* PostgreSQL database
* Environment variable based configuration

---

## 🏗️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** JWT (SimpleJWT)
* **Database:** PostgreSQL

---

## 📁 Project Structure

```
job_portal/
├── accounts/        # Custom user & authentication
├── recruiters/     # Recruiter profiles & job posting
├── jobs/            # Job listings
├── applications/   # Job applications
├── config/          # Settings, URLs, WSGI/ASGI
├── manage.py
├── requirements.txt
└── README.md
```
---

## ▶️ Run Locally

```bash
# Clone repository
git clone <repo-url>
cd job_portal

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## 🔐 API Authentication Flow

1. Register user (Recruiter / Job Seeker)
2. Login → receive **Access & Refresh token**
3. Pass token in headers:

```
Authorization: Bearer <access_token>
```

---

## 🧪 API Testing

* Tool: **Postman**
* Authentication: JWT Bearer Token
* Supports role-based access control

---

## 📈 Future Enhancements

* Resume upload & parsing
* Job search & filters
* Admin analytics dashboard
* Email notifications
* Frontend integration
