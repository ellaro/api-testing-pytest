
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['users']  # Replace with your database name
collection = db['data']  # Replace with your collection name


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


@app.route('/users', methods=['PUT'])
def update_user():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({"error": "Invalid input data"}), 400

    filter_query = {"email": data["email"]}

    set_data = {'email': data['new_email']}
    new_values = {"$set": set_data}

    user = collection.find_one_and_update(filter=filter_query, update=new_values)
    print(user)

    if not user:
        return jsonify({"error": "user not found"}), 404

    user["_id"] = str(user["_id"])
    return jsonify(user), 200


@app.route('/users', methods=['DELETE'])
def delete_user():
    data = request.get_json()

    user = collection.delete_one({"email": data['email']})
    if user:
        return jsonify({"message": "User deleted successfuly"}), 200
    else:
        return jsonify({"message": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)


