__author__ = 'manu'

class Job:

    def __init__(self, name, params):
        self.name = name
        self.params = params
        self.type = "default"

    def getInfo(self):
        return {"type": self.type, "name": self.name, "params": self.params}

    def run(self):
        pass