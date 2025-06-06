from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
