from flask import Flask, request, jsonify
from leave_service import submit_leave, approve_leave

app = Flask(__name__)

@app.route("/leave_requests", methods=["POST"])
def create_leave():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid input"}), 400

    result, code = submit_leave(data)
    return jsonify(result), code


@app.route("/approve/<employee_id>", methods=["PATCH"])
def approve(employee_id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid input"}), 400

    comment = data.get("comment", "")
    result, code = approve_leave(employee_id, comment)
    return jsonify(result), code


if __name__ == "__main__":
    app.run()