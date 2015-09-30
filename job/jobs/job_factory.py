from job.jobs.Job import Job
from job.jobs.PrintJob import PrintJob


def create_job(job_info):
    job_type = job_info["type"]
    if job_type == "default":
        return Job(job_info["name"], job_info["params"])
    elif job_type == "print":
        return PrintJob(job_info["name"], job_info["params"])