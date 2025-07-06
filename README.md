# 🍔 Burger E-Commerce App (Django)

This is a simple e-commerce web app for ordering burgers, built with **Python** and **Django**.

## 🛠️ Features

- ✅ Burger menu display
- 🛒 Add to cart functionality for each burger
- 🧾 Basic checkout page
- 👤 User login/logout system (not enabled)

This project is designed as a practice/demo app to understand how a basic food ordering system works using Django framework.

---

## 🚧 What’s Not Included in This Repo

To keep this repository clean and safe, the following files and folders have been **removed** from version control:

- `db.sqlite3` – Local development database file
- `migrations/` – Django migration files for apps
- `__pycache__/` – Python cache files
- `.env` – Any environment variable or secret keys
- `static/` & `media/` – Local static/media files (can be regenerated)

> ⚠️ You'll need to run `python manage.py makemigrations` and `python manage.py migrate` to generate fresh migrations and DB.

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/ammarproficient/burger.git
   cd burger
