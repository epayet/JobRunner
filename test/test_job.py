from default.Job import Job
from default.PrintJob import PrintJob

__author__ = 'manu'

import unittest


class TestJob(unittest.TestCase):
    def test_getInfo(self):
        jobName = "test"
        job = Job(jobName, {})
        jobInfo = job.getInfo()
        self.assertEqual(jobInfo, {"name": jobName, "type": "default", "params": {}})

    def test_runPrintJob(self):
        job = PrintJob("print", {"text": "hey coucou"})
        job.run()

    def test_getPrintJobInfo(self):
        jobName = "test"
        job = PrintJob(jobName, {})
        jobInfo = job.getInfo()
        self.assertEqual(jobInfo, {"name": jobName, "type": "print", "params": {}})