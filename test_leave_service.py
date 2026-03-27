from leave_service import submit_leave


def test_submit_leave_success():
    data = {
        "employee_id": "101",
        "start_date": "2026-03-28",
        "end_date": "2026-03-30",
        "leave_type": "Vacation",
        "reason": "Family Function"
    }

    result, code = submit_leave(data)

    if code != 200:
        raise Exception("Leave submission failed")


def test_missing_field():
    data = {
        "employee_id": "102",
        "start_date": "",
        "end_date": "2026-03-30",
        "leave_type": "Vacation",
        "reason": "Trip"
    }

    result, code = submit_leave(data)

    if code != 400:
        raise Exception("Validation failed")