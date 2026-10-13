import json
import random

class MemoryStore:

    def __init__(self):
        self.memories = []

    def add(self, memory):
        self.memories.append(memory)

    def load(self, filepath):

        with open(filepath, "r") as f:
            data = json.load(f)

        self.memories.extend(data)

    def retrieve(self, query, top_k=5):

        matches = []

        for memory in self.memories:

            if any(
                word.lower() in memory["text"].lower()
                for word in query.split()
            ):
                matches.append(memory)

        return matches[:top_k]

    def cleanup(self):
        self.memories.clear()

    def count(self):
        return len(self.memories)

    def poison_count(self):
        return len([
            m for m in self.memories
            if m.get("is_poison", False)
        ])