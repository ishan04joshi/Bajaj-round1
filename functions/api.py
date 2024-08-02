# functions/api.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

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

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

def handler(event, context):
    from netlify_lambda_wsgi import handler as wsgi_handler
    return wsgi_handler(app, event, context)

if __name__ == "__main__":
    app.run(debug=True)
