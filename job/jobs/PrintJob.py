from job.jobs.Job import Job


class PrintJob(Job):

    def __init__(self, name, params={}):
        Job.__init__(self, name, params)
        self.type = "print"

    def run(self):
        print(self.params["text"])
