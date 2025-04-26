
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    if not data or not 'name' in data or not 'email' in data:
        return jsonify({"error": "Invalid input data"}), 400

    new_user = {
        'name': data['name'],
        'email': data['email']
    }

    try:
        collection.insert_one(new_user)
    except Exception as e:
        print('insert error')
        print(e)

    try:
        json = jsonify(new_user)
    except Exception as e:
        print('jsonify error')
        print(e)

    return jsonify(new_user), 201


@app.route('/users/<email_var>', methods=['GET'])
def get_user(email_var):
    user = collection.find_one({"email": email_var})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/users/<email_var>', methods=['PUT'])
def update_user(email_var):
    user = collection.find_one_and_update({"email": email_var})
    if not email_var:
        return jsonify({"error": "user not found"}), 404
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    updated_data = {
        "name": data.get("name", user.get("name")),
        "email": data.get("email", user.get("email"))
    }
    collection.update_one({"email": email_var}, {"$set": updated_data})
    user.update(updated_data)
    user["_id"] = str(user["_id"])

    return jsonify(user)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if user:
        return jsonify({"message": "User deleted successfuly"}), 200
    else:
        return jsonify({"message": "User not found"}), 404


if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
    db = client['users']  # Replace with your database name
    collection = db['data']  # Replace with your collection name
    app.run(debug=True)


