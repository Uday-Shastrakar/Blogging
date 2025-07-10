# ✍️ Blogging Platform

A full-featured blogging application built with Django. Users can create, edit, publish, and comment on blog posts. Includes admin panel, authentication, and clean UI for easy content management.

## 🌟 Features

- User registration and login system
- Create, update, delete blog posts
- Rich text editing for content (Markdown/HTML)
- Commenting system for posts
- Draft/publish control for bloggers
- SEO-friendly URLs and slugs
- Django admin panel for backend control

## 🧰 Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Backend     | Python, Django         |
| Frontend    | HTML, CSS, Bootstrap   |
| Database    | SQLite (default), can switch to PostgreSQL or MySQL |
| Auth        | Django Auth (Sessions) |

## 📂 Project Structure

blog-project/
├── blog/ # Core blog app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/blog/
├── users/ # Custom user auth
├── static/ # CSS, JS, images
├── media/ # Uploaded content
├── blog_project/ # Project settings
│ └── settings.py
├── db.sqlite3
└── manage.py

bash
Copy
Edit

## ⚙️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Uday-Shastrakar/blogging-django.git
cd blogging-django
2. Create a virtual environment and install dependencies
bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
3. Run migrations and start server
bash
Copy
Edit
python manage.py migrate
python manage.py createsuperuser  # To access admin panel
python manage.py runserver
Visit http://127.0.0.1:8000/ to use the app.

🔐 Admin Panel
URL: /admin/

Use the superuser credentials created earlier

📸 Screenshots
Add images of post list, post editor, comments, etc.

🧠 Concepts Used
Django Class-Based Views (CBVs)

Django ORM and Querysets

Django Templates and Template Inheritance

Static & Media file handling

Authentication & Authorization

📌 Future Enhancements
Add tags and categories for posts

Like/bookmark system

REST API for mobile/frontend integration

WYSIWYG editor (like TinyMCE)

👨‍💻 Developed By
Uday Shastrakar
📧 uday.shastrakar@gmail.com
🌐 GitHub | Portfolio
