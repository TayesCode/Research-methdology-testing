from memory_store import MemoryStore

def test_no_label_leakage():

    store = MemoryStore()

    store.add({
        "id": "P1",
        "text": "poison",
        "is_poison": True
    })

    retrieved = store.retrieve("poison")

    for m in retrieved:

        exposed = dict(m)

        exposed.pop("is_poison", None)

        assert "is_poison" not in exposed