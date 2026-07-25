<div align="center">

# 🏋️ Fitness Enhancer

**A modern, full-stack fitness web application built with Django.**

*Helping users manage their fitness journey through personalized workout planning, nutrition tracking, and progress monitoring.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/saninfuhad763-collab/Fitness-Enhancer)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

## 🔍 Overview

**Fitness Enhancer** is a full-stack web application built with Django that provides users with a centralized platform for managing their health and fitness activities. The application features a clean, dark-mode UI with a custom design system, offering tools for tracking nutrition, generating personalized workout plans, monitoring body progress, and managing a user profile — all behind a secure authentication layer.

This project demonstrates end-to-end Django development skills including custom user models, model-driven logic, template inheritance, static asset management, and a tiered subscription model (free vs. premium).

---

## ✨ Features

### 🔐 Authentication & User Management
- Secure user registration and login with Django's built-in authentication
- Session-based access control protecting all authenticated pages
- User profile management (weight, height, fitness goal, activity level)

### 🏠 Personalized Dashboard
- At-a-glance overview of key metrics: current weight, BMI, and primary fitness goal
- Activity overview chart (Chart.js) with a weekly view
- Quick navigation to all major app sections

### 🥗 Nutrition Dashboard
- Personalized calorie and macronutrient targets calculated from user profile data
- Locked premium features visible with upgrade prompts for free-tier users

### 🏋️ Workout Planner
- Deterministic workout plan generator tailored to user goals and activity level
- Weekly schedule view for premium subscribers
- Exercise listings with clear structure

### 📈 Progress Tracker
- Log and monitor body weight and fitness metrics over time
- Visualized progress to support goal accountability

### 💎 Premium Upgrade Page
- Clear, structured comparison of free vs. premium features
- Professional upgrade flow with feature highlights

### 🛠️ Developer-Quality Details
- Custom-designed `404` and `500` error pages consistent with the app's design language
- Responsive layout across desktop and tablet viewports
- WhiteNoise-powered static file serving

---

## 🧰 Tech Stack

| Category | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **Framework** | Django 4.x |
| **Frontend** | HTML5, CSS3, JavaScript (ES6) |
| **UI Library** | Bootstrap 5.3 |
| **Charts** | Chart.js |
| **Icons** | Bootstrap Icons, Lucide Icons |
| **Database** | SQLite |
| **Static Files** | WhiteNoise |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
fitness-enhancer/
│
├── config/                  # Django project settings and URL configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/                   # User authentication, profiles, and subscriptions
│   ├── models.py            # UserProfile, Subscription models
│   ├── views.py
│   └── urls.py
│
├── workouts/                # Workout plan generation and weekly scheduling
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── nutrition/               # Calorie and macronutrient tracking
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── progress/                # Body metrics and progress logging
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── tools/                   # Utility calculators (e.g., calorie estimator)
│   └── views.py
│
├── templates/               # Django HTML templates (organized by app)
│   ├── base/
│   │   └── base.html        # Master layout with navbar
│   ├── dashboard/
│   ├── workouts/
│   ├── nutrition/
│   ├── progress/
│   ├── users/
│   └── auth/
│
├── static/
│   └── css/
│       └── style.css        # Custom design system (dark mode, glassmorphism)
│
├── staticfiles/             # Collected static files (auto-generated)
├── manage.py
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` package manager
- `git`

### 1. Clone the Repository

```bash
git clone https://github.com/saninfuhad763-collab/Fitness-Enhancer.git
cd Fitness-Enhancer
```

### 2. Create and Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser *(Optional)*

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📸 Screenshots

> *Screenshots will be added here once the project reaches a stable UI milestone.*

| Page | Preview |
|---|---|
| Dashboard | *(Coming soon)* |
| Workout Planner | *(Coming soon)* |
| Nutrition Dashboard | *(Coming soon)* |
| Progress Tracker | *(Coming soon)* |
| Upgrade Page | *(Coming soon)* |

---

## 🔭 Future Improvements

The following enhancements are planned for future development iterations:

- [ ] **Food Database Integration** — connect to a nutrition API (e.g., Open Food Facts) for real-time meal logging
- [ ] **AI-Powered Workout Suggestions** — dynamically adjust plans based on logged performance
- [ ] **Actual Progress Charts** — replace demo data with user-submitted progress visualizations
- [ ] **Cloud Deployment** — host on a platform such as Railway or Render with PostgreSQL
- [ ] **REST API Layer** — expose core functionality via Django REST Framework for mobile client support
- [ ] **Email Notifications** — weekly progress summaries and workout reminders
- [ ] **Dark / Light Mode Toggle** — user-selectable theme preference
- [ ] **Unit & Integration Tests** — comprehensive test coverage using `pytest-django`

---

## 👤 Author

**Sanin Fuhad**

- GitHub: [@saninfuhad763-collab](https://github.com/saninfuhad763-collab)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

*Built with dedication as a full-stack Django portfolio project.*

</div>
