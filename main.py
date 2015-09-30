from job.JobRunner import JobRunner
from job.jobs.PrintJob import PrintJob
from job.queue.RedisQueue import RedisQueue

if __name__ == "__main__":
    redis_queue = RedisQueue()
    job_runner = JobRunner(redis_queue)

    for i in range(0, 20):
        job_runner.add_job(PrintJob({"text": i}))

    job_runner.run()
    # it should print 20 times using redis queue
