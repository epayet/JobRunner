import os
import time
import socket

from job.JobRunner import JobRunner
from job.jobs.PrintJob import PrintJob
from job.queue.RedisQueue import RedisQueue

if __name__ == "__main__":
    redis_addr = os.environ.get("REDIS_PORT_6379_TCP_ADDR")
    redis_port = os.environ.get("REDIS_PORT_6379_TCP_PORT")
    machine_name = socket.gethostname()

    redis_queue = RedisQueue(redis_addr, redis_port)
    job_runner = JobRunner(redis_queue)

    # Send a new job every second
    i = 0
    while True:
        job_runner.add_job(PrintJob("test", {"text": machine_name + ": job " + str(i) + " consumed"}))
        i += 1
        print("Machine " + machine_name + " added job " + str(i))
        time.sleep(5)
