# 🔐 Document Security Scanner (Django)

This project is a web-based document security system built using Django. It allows users to upload files and performs security checks to detect potentially malicious or unsafe content.

The system ensures that uploaded documents are verified before being processed or stored, making it useful for secure file handling applications.

---

## 🚀 Features

* 📁 File upload and management system
* 🔍 Document scanning for potential threats
* 🛡️ Basic malware/suspicious content detection
* ⚙️ Backend processing using Django
* 🧩 Modular architecture (scanner + security modules)

---

## 🏗️ Project Structure

```
verification-project/
│
├── security/              # Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── scanner/               # Core scanning app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│
├── venv/                  # Virtual environment (ignored)
├── manage.py              # Entry point
```

---

## ⚙️ How It Works

1. User uploads a document through the interface
2. The file is sent to the backend
3. Scanner module analyzes the file
4. System checks for suspicious or unsafe patterns
5. Output is generated:

   * ✅ Safe file
   * ⚠️ Potentially unsafe file

---

## 🛠️ Tech Stack

* Python
* Django
* SQLite (default database)
* HTML (templates)

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/your-username/doc-security-scanner.git
```

2. Navigate to project folder:

```
cd verification-project
```

3. Activate virtual environment:

```
venv\Scripts\activate
```

4. Install dependencies:

```
pip install django
```

5. Run migrations:

```
python manage.py migrate
```

6. Start server:

```
python manage.py runserver
```

7. Open in browser:

```
http://127.0.0.1:8000/
```

---

## ⚠️ Notes

* This project demonstrates **basic document security concepts**
* Not a full antivirus system
* Can be extended using:

  * VirusTotal API
  * Machine learning models
  * File signature analysis

---

## 👩‍💻 Author

Shreya
