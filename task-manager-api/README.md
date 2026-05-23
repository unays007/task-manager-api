# ✅ Task Manager REST API

A powerful **Task Management REST API** built with **Python Django REST Framework**, featuring JWT authentication, task filtering, categories, and statistics.

## 🚀 Tech Stack

- **Python 3.11**
- **Django 4.2**
- **Django REST Framework**
- **Simple JWT** (Authentication)
- **SQLite** (development)
- **CORS Headers**

## ✨ Features

- ✅ User registration & JWT login
- ✅ Create, read, update, delete tasks
- ✅ Task categories
- ✅ Filter by status, priority, category
- ✅ Search tasks by title/description
- ✅ Task statistics (total, todo, in progress, done)
- ✅ Priority levels: Low / Medium / High
- ✅ Status: To Do / In Progress / Done

## 🔧 Getting Started

```bash
git clone https://github.com/unays007/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API runs on: `http://localhost:8000`

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register |
| POST | `/api/auth/login/` | Login & get JWT |
| GET | `/api/tasks/` | Get all tasks |
| POST | `/api/tasks/` | Create task |
| GET | `/api/tasks/{id}/` | Get task |
| PUT | `/api/tasks/{id}/` | Update task |
| DELETE | `/api/tasks/{id}/` | Delete task |
| GET | `/api/tasks/stats/` | Task statistics |
| GET | `/api/categories/` | Get categories |
| POST | `/api/categories/` | Create category |

## 🔐 Authentication

```
Authorization: Bearer <your_jwt_token>
```

## 🔍 Filtering & Search

```
GET /api/tasks/?status=todo
GET /api/tasks/?priority=high
GET /api/tasks/?search=meeting
GET /api/tasks/?ordering=-due_date
```

## 📝 Example

```json
POST /api/tasks/
{
  "title": "Fix login bug",
  "description": "JWT token not refreshing",
  "status": "in_progress",
  "priority": "high",
  "due_date": "2024-12-31"
}
```

## 👨‍💻 Built by Unays Y. — Full-Stack Developer
