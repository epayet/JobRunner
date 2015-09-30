from job.jobs.job_factory import create_job


class JobRunner:
    def __init__(self, queue):
        self.queue = queue

    def add_job(self, job):
        info = job.get_info()
        self.queue.push(info)

    def get_nb_jobs(self):
        return self.queue.get_nb_data()

    def clear_jobs(self):
        self.queue.clear_queue()

    def run(self):
        job_info = self.queue.pop()
        job = create_job(job_info)
        job.run()
