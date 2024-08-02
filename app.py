# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()

    if not data or "data" not in data:
        return jsonify({
            "is_success": False,
            "user_id": "",
            "email": "",
            "roll_number": "",
            "numbers": [],
            "alphabets": [],
            "highest_alphabet": []
        })

    full_name = "john_doe"  # Replace with actual full name
    dob = "17091999"       # Replace with actual date of birth
    email = "john@xyz.com"  # Replace with actual email
    roll_number = "ABCD123" # Replace with actual roll number

    user_id = f"{full_name}_{dob}"

    numbers = [item for item in data["data"] if item.isdigit()]
    alphabets = [item for item in data["data"] if item.isalpha()]
    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run()
