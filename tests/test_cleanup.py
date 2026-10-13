from memory_store import MemoryStore

def test_cleanup():

    store = MemoryStore()

    store.add(
        {
            "id":"A",
            "text":"sample"
        }
    )

    store.cleanup()

    assert store.count() == 0