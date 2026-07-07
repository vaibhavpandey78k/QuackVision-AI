progress = {
    "progress": 0,
    "step": "Waiting...",
    "completed": [],
    "status": "idle"
}


def update_progress(percent, step):
    progress["progress"] = percent
    progress["step"] = step

    if step not in progress["completed"]:
        progress["completed"].append(step)

    progress["status"] = "processing"


def complete():
    progress["progress"] = 100
    progress["step"] = "Completed"
    progress["status"] = "completed"


def get_progress():
    return progress


def reset_progress():
    progress["progress"] = 0
    progress["step"] = "Starting..."
    progress["completed"] = []
    progress["status"] = "processing"