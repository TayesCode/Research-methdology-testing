import hashlib

def hash_text(text):

    return hashlib.sha256(
        text.encode()
    ).hexdigest()

def test_benchmark_equality():

    d1 = hash_text("same dataset")
    d2 = hash_text("same dataset")

    assert d1 == d2