# 🧪 Flask MongoDB User API

This is a simple RESTful API built with **Flask** and **MongoDB**, enabling full CRUD operations (Create, Read, Update, Delete) for user data. The project includes Docker support and Pytest-based automated tests.

---

## 📁 Project Structure

```
project/
├── src/
│   ├── main.py          # Flask app with endpoints
│   └── tests.py         # Pytest test cases
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container setup
└── README.md            # Project documentation
```

---

## ⚙️ Python Environment Setup

1. Make sure you have **Python 3.10+** installed.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Flask RESTful Server

```bash
python ./src/main.py
```

The API will be available at `http://localhost:5000`.

---

## ✅ Run Pytest Tests

To execute automated tests:

```bash
python -m pytest ./src/tests.py
```

Ensure your local MongoDB server is running and reachable at `mongodb://localhost:27017/`.

---

## 🐳 Run with Docker

### 1. Build Docker image:

```bash
docker build -t flask-user-api ./src
```

### 2. Run Docker container:

```bash
docker run -p 5000:5000 flask-user-api
```

### Dockerfile Overview

```dockerfile
FROM python:3.10

WORKDIR /ella

COPY main.py requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "main.py"]
```

> 📌 You can modify `main.py` to use relative paths (like `src/main.py`) if needed.

---

## 📌 Notes

- The app uses MongoDB and stores user data in the `users` database and `data` collection.
- The tests in `tests.py` include:
  - Fetching an existing user (`Dsoron@gmail.com`)
  - Fetching a non-existent user (should return 404)
- You can expand the test coverage using the modular design of the code.

---

## 🧰 Tech Stack

- **Flask** – lightweight web framework
- **PyMongo** – MongoDB integration for Python
- **Pytest** – testing framework
- **Docker** – containerization
---

## 🏷 Tags

`#flask` `#mongodb` `#api` `#python` `#docker` `#pytest` `#restful` `#automation` `#qa`

---

## 👩‍💻 Author

Made with ❤️ by a passionate QA and Python developer.
