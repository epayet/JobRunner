from default.Job import Job
from default.PrintJob import PrintJob

__author__ = 'manu'

import redis

class JobRunner:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.jobQueueKey = "jobQueue"

    def addJob(self, job):
        jobInfo = job.getInfo()
        self.redis.lpush(self.jobQueueKey, jobInfo)

    def getNbJobs(self):
        return self.redis.llen(self.jobQueueKey)

    def clearJobs(self):
        self.redis.delete(self.jobQueueKey)

    def run(self):
        jobInfo = eval(self.redis.lpop(self.jobQueueKey))
        job = self._createJob(jobInfo)
        job.run()

    def _createJob(self, jobInfo):
        #TODO refactoring: create class from string
        type = jobInfo["type"]
        if type == "default":
            return Job(jobInfo["name"], jobInfo["params"])
        elif type == "print":
            return PrintJob(jobInfo["name"], jobInfo["params"])