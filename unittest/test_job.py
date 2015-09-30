import unittest

from job.jobs.Job import Job
from job.jobs.PrintJob import PrintJob


class TestJob(unittest.TestCase):
    def test_getInfo(self):
        job = Job("test", {'test': 'test'})
        job_info = job.get_info()
        self.assertEqual(job_info, {"name": "test", "type": "default", "params": {'test': 'test'}})

    def test_getPrintJobInfo(self):
        job = PrintJob("test")
        job_info = job.get_info()
        self.assertEqual(job_info, {"name": "test", "type": "print", "params": {}})
