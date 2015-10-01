import os

from job.JobRunner import JobRunner
from job.jobs.PrintJob import PrintJob
from job.queue.MemoryQueue import MemoryQueue
from job.queue.RedisQueue import RedisQueue

if __name__ == "__main__":
    redis_addr = os.environ.get("REDIS_PORT_6379_TCP_ADDR")
    redis_port = os.environ.get("REDIS_PORT_6379_TCP_PORT")

    redis_queue = RedisQueue(redis_addr, redis_port)
    # memory_queue = MemoryQueue()

    job_runner = JobRunner(redis_queue)
    # job_runner = JobRunner(memory_queue)

    for i in range(0, 20):
        job_runner.add_job(PrintJob("test", {"text": i}))

    job_runner.run()
    # it should print 20 times using redis queue
