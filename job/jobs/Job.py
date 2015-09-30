class Job:
    def __init__(self, name, params={}):
        self.name = name
        self.params = params
        self.type = "default"

    def get_info(self):
        return {"type": self.type, "name": self.name, "params": self.params}

    def run(self):
        pass
