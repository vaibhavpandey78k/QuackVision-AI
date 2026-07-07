import uuid

jobs = {}

def create_job():
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "progress": 0,
        "step": "Starting...",
        "status": "processing",
        "result": None
    }

    return job_id


def update_job(job_id, progress, step):
    if job_id in jobs:
        jobs[job_id]["progress"] = progress
        jobs[job_id]["step"] = step


def finish_job(job_id, result):
    if job_id in jobs:
        jobs[job_id]["progress"] = 100
        jobs[job_id]["step"] = "Completed"
        jobs[job_id]["status"] = "completed"
        jobs[job_id]["result"] = result


def get_job(job_id):
    return jobs.get(job_id)