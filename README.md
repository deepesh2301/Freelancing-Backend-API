# Freelancing Platform Backend API

A complete role-based Freelancing Platform Backend built using **FastAPI**, **SQLAlchemy**, **MySQL**, and **JWT Authentication**.

This application allows clients to post projects, freelancers to submit proposals, clients to hire freelancers, manage contracts, process payments, submit reviews, and view personalized dashboards.

---

# Features

## Authentication
- User Registration
- User Login
- JWT Authentication
- Role-Based Authorization (Client / Freelancer)

## Project Management
- Create Project
- Update Project
- Delete Project
- View All Projects
- View Single Project

## Proposal Management
- Freelancer can apply for projects
- Prevent duplicate proposals
- Client can view all proposals
- Accept one proposal
- Automatically reject remaining proposals

## Contract Management
- Automatic contract creation after proposal acceptance
- Active and Completed contract status
- View contract details

## Payment Management
- Client can make payment
- Payment linked with contract
- Payment history

## Review & Rating
- Client reviews Freelancer
- Freelancer reviews Client
- Prevent duplicate reviews
- Average rating calculation

## Dashboard

### Client Dashboard
- Total Projects
- Active Contracts
- Completed Contracts
- Total Payments

### Freelancer Dashboard
- Total Proposals
- Accepted Proposals
- Active Contracts
- Completed Contracts
- Total Earnings
- Average Rating

---

# Tech Stack

- Python 3
- FastAPI
- SQLAlchemy ORM
- MySQL
- JWT Authentication
- Pydantic
- Uvicorn

---

# Project Structure

```text
Freelancing-Backend/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# Installation

### Clone the repository

```bash
git clone <repository-url>
cd Freelancing-Backend
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and add your database and JWT configuration.

Example:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/FreelanceDB

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run the project

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

# API Modules

- Authentication
- Projects
- Proposals
- Contracts
- Payments
- Reviews
- Dashboard

---

# Database Tables

- Users
- Roles
- Projects
- Proposals
- Contracts
- Payments
- Reviews

---

# Future Improvements

- File Upload
- Chat System
- Notifications
- Admin Panel
- Search & Filters
- Email Notifications
- Docker Support
- CI/CD Pipeline

---

# Author

**Deepesh Sahu**

- MCA Graduate
- Python Backend Developer
- FastAPI | SQLAlchemy | MySQL | JWT

---

# License

This project is developed for educational and portfolio purposes.