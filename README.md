# 🚀 Servers Management API

REST API built with FastAPI to manage servers (name + IP) with JSON data persistence.

---

## 📌 Features

- Add a server
- List all servers
- Delete a server
- Validate IP addresses
- Persistent storage using a JSON file

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- Uvicorn
- Pydantic

---

## ⚙️ Prerequisites

- Python 3.x
- pip

Check installation:

```bash
python --version
pip --version
```

---

## ▶️ Installation & Run

```bash
# Clone the repository
git clone https://github.com/quentin-juskowiak/servers-management-api.git
cd servers-management-api

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload
```

---

## 🌐 API Access

- Swagger UI: http://127.0.0.1:8000/docs  
- ReDoc: http://127.0.0.1:8000/redoc  

---

## 🧪 Example Request

### POST /servers

```json
{
  "name": "Web Server",
  "ip": "192.168.1.10"
}
```

---

## 🔁 Available Endpoints

- GET / → API status  
- GET /servers → List all servers  
- POST /servers → Add a server  
- DELETE /servers/{server_id} → Delete a server  

---

## 📂 Project Structure

```
servers-management-api/
│── main.py
│── servers.json
│── requirements.txt
│── .gitignore
```

---

## 💾 Data Storage

- Data is stored in `servers.json`
- Data persists after restarting the API

---

## ⚠️ Notes

- This project is for learning purposes
- No authentication implemented
- Data is stored locally

---

## 🚀 Possible Improvements

- Add database (SQLite)
- Add authentication (JWT)
- Add update endpoint (PUT / PATCH)
- Dockerize the application

---

## 👨‍💻 Author

Quentin Juskowiak
