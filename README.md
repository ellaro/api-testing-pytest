# Flask MongoDB User API

A lightweight RESTful API built with Flask and MongoDB for basic user management operations (Create, Read, Update, Delete).

## 🚀 Features

- ✅ **Create User** – Add a new user with name and email.
- ✅ **Get User** – Retrieve a user by email.
- ✅ **Update User** – Update user's email.
- ✅ **Delete User** – Remove user by email.
- ✅ **Docker Support** – Run the app easily in a container.
- ✅ **Pytest Unit Tests** – Includes basic automated tests.

## 🧠 Tech Stack

- Python 3.10
- Flask
- PyMongo
- MongoDB
- Pytest
- Docker

## 📂 Project Structure

```
/ella
├── main.py             # Flask app
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker setup
├── tests.py            # Pytest test file
└── README.md           # Project documentation
```

## 📦 Requirements

Install required dependencies:

```bash
pip install -r requirements.txt
```

Ensure you have a local MongoDB instance running on:

```
mongodb://localhost:27017/
```

## ▶️ Run the Flask Server

```bash
python main.py
```

## 🧪 Run Tests

You can run the automated tests using:

```bash
python -m pytest ./tests.py
```

Or, if your tests are inside a `src/` folder:

```bash
python -m pytest ./src/tests.py
```

## 🐳 Run with Docker

Build and run using Docker:

```bash
docker build -t flask-api .
docker run -p 5000:5000 flask-api
```

## 📌 Notes

- The app automatically creates the `users` database and the `data` collection.
- The email used in tests must already exist in the database (`Dsoron@gmail.com` is used in `test_get_existing_user`).
- You can modify the database/collection name in `main.py`.

## 🏆 Credits

Developed using:
- Flask Web Framework
- PyMongo for MongoDB integration
- Pytest for testing

## 🏷 Tags

`#flask` `#mongodb` `#api` `#python` `#docker` `#pytest` `#qa` `#automation`

