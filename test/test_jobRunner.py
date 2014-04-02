from unittest import TestCase

from default.JobRunner import JobRunner
from default.Job import Job
from default.PrintJob import PrintJob


__author__ = 'manu'

class TestJobRunner(TestCase):
    def setUp(self):
        self.jobRunner = JobRunner()

    def tearDown(self):
        self.jobRunner.clearJobs()

    def test_getNbJobs_empty(self):
        self.assertEqual(self.jobRunner.getNbJobs(), 0)

    def test_createJob_JobCreated(self):
        job = Job("test", {})
        self.jobRunner.addJob(job)
        self.assertEqual(self.jobRunner.getNbJobs(), 1)

    def test_runPrintJob_JobPopped(self):
        job = PrintJob("PrintJobCoucouToi", {"text": "coucou toi"})
        self.jobRunner.addJob(job)
        self.jobRunner.run()
        self.assertEqual(self.jobRunner.getNbJobs(), 0)