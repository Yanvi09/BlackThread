# 🧠 BlackThread Secure Ops Interface

> **Codename:** Project BlackThread  
> **Lead Developer:** Anvi Yadav  
> **Mission:** Secure. Monitor. Dominate.  

---

## 🎯 Overview

**BlackThread** is a high-security, tactical operations interface built for elite engineering units managing classified assets, covert missions, and cyber threat intelligence. Designed to resemble a futuristic command console, this system is both visually striking and functionally airtight.

This full-stack Django-based project simulates real-world deployment and operations management within a secure organization — from engineer rosters to threat logging and mission dispatching.

---

## 🛠️ Tech Stack

| Layer       | Tech Used                     |
|-------------|-------------------------------|
| 💻 Frontend | Django Templates + Bootstrap  |
| 🎨 Styling  | Custom CSS (Orbitron theme)   |
| 🧠 Backend  | Python, Django, Django REST Framework |
| 🧾 Database | SQLite3                        |
| 📊 Charts   | Chart.js                       |
| 🔐 Auth     | DRF Token Authentication       |

---

## 🧩 Features

### 👨‍💻 Engineers
- Add, edit, remove field engineers
- Grouped dynamically by specialty
- Display clearance levels and contact info

### 🧰 Assets
- Track gear, equipment, and tech in use
- View and manage status (assigned/unassigned)

### 🎯 Missions
- Deploy engineers and assign assets
- Set urgency levels and mission status
- Live dashboard overview of operations

### 🚨 Threat Logs
- Log and view security breaches or alerts
- Linked to missions for audit trails

### 📋 Activity Logs
- View backend activity & interactions

### 📊 Dashboard
- Traffic monitoring using Chart.js
- Target scanner animation via Lottie
- Quick-access launchpad for all sections

---

## 🧪 API Endpoints

BlackThread includes REST API support with Token Authentication.

| Endpoint | Description |
|----------|-------------|
| `/api/engineers/` | List/Create engineers |
| `/api/assets/`    | List/Create assets    |
| `/api/missions/`  | List/Create missions  |
| `/api/threats/`   | List/Create threats   |

🔒 All API routes require a valid token in the request header


---

## 🚀 How to Run Locally

### 1. Clone the Repo

git clone https://github.com/your-username/blackthread-ops.git
cd blackthread-ops

2. Create Virtual Environment
   
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

3. Install Requirements

   pip install -r requirements.txt

4. Migrate Database

   python manage.py migrate

5. Create Superuser (for admin access)

   python manage.py createsuperuser

6. Run the Server

   python manage.py runserver
   --> Visit: http://127.0.0.1:8000

7. Token Setup for API

Inside Django shell:

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.get(username='your_username')
token, created = Token.objects.get_or_create(user=user)
print(token.key)

Use this token in Postman or Thunder Client to access protected endpoints.

📂 Folder Structure
```bash
blackthread/
│
├── core/               # Main app
│   ├── models.py       # Engineer, Asset, Mission, Threat
│   ├── views.py        # UI views
│   ├── urls.py         # URL routing
│   ├── templates/      # All HTML files
│
├── api/                # DRF API app
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── static/             # Custom CSS, JS (if needed)
├── db.sqlite3          # Database file
├── manage.py
└── README.md
```





   


