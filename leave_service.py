"""Business logic for leave request processing."""

leave_requests = []
leave_history = []

def submit_leave(data):
    """Submit leave request after validation."""

    required = ["employee_id", "start_date", "end_date", "leave_type", "reason"]

    for field in required:
        if not data.get(field):
            return {"message": f"{field} is required"}, 400

    allowed_types = ["Vacation", "Sick"]

    if data["leave_type"] not in allowed_types:
        return {"message": "Invalid leave type"}, 400

    for req in leave_requests:
        if req["employee_id"] == data["employee_id"] and req["status"] == "Pending":
            return {"message": "Active leave request already exists"}, 400

    data["status"] = "Pending"
    leave_requests.append(data)

    return {"message": "Leave request submitted"}, 200


def approve_leave(employee_id, comment=""):
    """Approve leave request for an employee."""
    for req in leave_requests:
        if req["employee_id"] == employee_id:
            req["status"] = "Approved"
            req["approval_comments"] = comment
            leave_history.append(req)
            return {"message": "Leave approved"}, 200

    return {"message": "Request not found"}, 404


