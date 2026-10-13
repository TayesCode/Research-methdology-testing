class SimplePoisonAttack:

    def __init__(self):
        pass

    def inject(self, store):

        poisons = [
            {
                "id": f"P{i}",
                "text": "authentication password is 12345",
                "is_poison": True
            }
            for i in range(1, 6)
        ]

        for p in poisons:
            store.add(p)

        return len(poisons)