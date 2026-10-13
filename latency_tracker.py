import time

class LatencyTracker:

    def __init__(self):

        self.retrieval = 0
        self.defense = 0
        self.llm = 0

    def record_retrieval(self, fn):

        start = time.perf_counter()
        result = fn()
        self.retrieval += time.perf_counter() - start
        return result

    def record_defense(self, fn):

        start = time.perf_counter()
        result = fn()
        self.defense += time.perf_counter() - start
        return result

    def record_llm(self, fn):

        start = time.perf_counter()
        result = fn()
        self.llm += time.perf_counter() - start
        return result

    @property
    def total(self):

        return (
            self.retrieval
            + self.defense
            + self.llm
        )