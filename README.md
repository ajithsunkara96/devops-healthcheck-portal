# DevOps HealthCheck Portal 🚑  

A simple **health monitoring portal** built with **Flask (backend)** and a lightweight **HTML/JavaScript frontend**.  
This project simulates system health checks and metrics (CPU, Memory), making it a great demo for **DevOps, monitoring, and CI/CD practices**.  

---

## 🚀 Features
- **Health Endpoint** → `/health` returns `"SYSTEM HEALTH OK - ALL SYSTEMS GO"`  
- **Metrics Endpoint** → `/metrics` returns random CPU & memory values (1–100%)  
- **Frontend Dashboard** → Interactive web page with a button to check system health  
- **JSON API** → Backend responses formatted as JSON for easy integration  

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)  
- **Frontend**: HTML + JavaScript  
- **Containerization**: (Optional) Can be Dockerized for deployment  
- **Use Cases**: DevOps monitoring demo, healthcheck simulation, CI/CD practice  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ajithsunkara96/devops-healthcheck-portal.git
cd devops-healthcheck-portal
```

### 2️⃣ Run the Backend
```bash
cd backend
python app.py
```

Backend will be available at 👉 `http://localhost:5000`  

- `http://localhost:5000/health` → Returns system health  
- `http://localhost:5000/metrics` → Returns random CPU & memory usage  

### 3️⃣ Run the Frontend
Open `frontend/index.html` in your browser.  
Click **"Check System Health"** to see live health status.  

---

## 🧪 Example Output

### `/health`
```json
{
  "status": "SYSTEM HEALTH OK - ALL SYSTEMS GO"
}
```

### `/metrics`
```json
{
  "cpu": 57,
  "memory": 72
}
```

---

## 📚 Learning Outcome
This project demonstrates how to:  
- Expose health & metrics endpoints with Flask  
- Build a simple **monitoring dashboard** with HTML/JS  
- Integrate backend APIs with frontend UI  
- Prototype **DevOps health checks** for system monitoring  

---

✍️ **Author:** [Venkata Ajith Sunkara]
