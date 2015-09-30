import unittest
from job.queue.MemoryQueue import MemoryQueue


class TestMemoryQueue(unittest.TestCase):
    def setUp(self):
        self.memory_queue = MemoryQueue()
