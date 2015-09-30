from unittest import TestCase

from job.JobRunner import JobRunner
from job.jobs.Job import Job
from job.queue.MemoryQueue import MemoryQueue


class TestJobRunner(TestCase):
    def setUp(self):
        memory_queue = MemoryQueue()
        self.job_runner = JobRunner(memory_queue)
        self.simple_job = Job("test")

    def test_getNbJobs_empty(self):
        self.assertEqual(self.job_runner.get_nb_jobs(), 0)

    def test_createJob_jobCreated(self):
        self.job_runner.add_job(self.simple_job)
        self.assertEqual(self.job_runner.get_nb_jobs(), 1)

    def test_run_1JobPopped(self):
        self.job_runner.add_job(self.simple_job)
        self.job_runner.run()
        self.assertEqual(self.job_runner.get_nb_jobs(), 0)

    def test_run_everyJob(self):
        self.job_runner.add_job(self.simple_job)
        self.job_runner.add_job(self.simple_job)
        self.job_runner.run()
        self.assertEqual(self.job_runner.get_nb_jobs(), 0)
