import os
import time

from job.JobRunner import JobRunner
from job.queue.RedisQueue import RedisQueue

if __name__ == "__main__":
    redis_addr = os.environ.get("REDIS_PORT_6379_TCP_ADDR")
    redis_port = os.environ.get("REDIS_PORT_6379_TCP_PORT")

    redis_queue = RedisQueue(redis_addr, redis_port)
    job_runner = JobRunner(redis_queue)

    # Run every job it can, then wait 1 second
    i = 0
    while True:
        job_runner.run()
        print("Every job consumed, waiting")
        time.sleep(5)
