import time

class Metrics:
    def __init__(self):
        self.start_time = time.time()

    def get_runtime(self):
        return time.time() - self.start_time