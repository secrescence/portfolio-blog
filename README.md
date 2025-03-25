# Portfolio + Blog Django Project

## 📁 Project Structure

```
portfolio_blog/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── portfolio/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── portfolio_app/
│   ├── migrations/
│   ├── static/portfolio_app/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── .gitignore
└── requirements.txt
```

---

## ✅ Project Overview
This project includes:
- A fully functional **Blog app** with Create, Read, Update, Delete (CRUD) functionalities.
- A simple **Portfolio app** to showcase projects or personal information.
- Clean and responsive Bootstrap-based UI styling.

---

## 🛠 How to Run

1. **Clone the repository:**
```
git clone https://github.com/secrescence/portfolio-blog
cd portfolio_blog
```

2. **Create a virtual environment:**
```
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate    # For Windows
```

3. **Install requirements:**
```
pip install -r requirements.txt
```

4. **Apply migrations:**
```
python manage.py migrate
```

5. **Create a superuser (optional):**
```
python manage.py createsuperuser
```

6. **Run the development server:**
```
python manage.py runserver
```

7. **Access the site:**
- Blog: `http://127.0.0.1:8000/blog/`
- Portfolio: `http://127.0.0.1:8000/`

---

## 📋 Features
- Blog Post creation with categories (Tech, Life, Tutorial, News)
- Edit and delete blog posts
- View blog details with clean layout
- Portfolio landing page ready for customization

---

## 📸 Screenshots

### Portfolio Homepage
<img width="773" alt="portfolio_home" src="https://github.com/user-attachments/assets/614d12da-0530-498c-be09-dc2e661285dd" />

### Blog Homepage
<img width="771" alt="blog_home" src="https://github.com/user-attachments/assets/87e1e819-5f40-4afa-9199-9ef674c85e72" />

---

## ✏️ Author
- Edsel Pisueña
- edselpisuena@gmail.com
- [LinkedIn](https://www.linkedin.com/in/edselpisue%C3%B1a/)

## 📧 Contact
If you have any questions or suggestions, feel free to reach out via LinkedIn or Email!
