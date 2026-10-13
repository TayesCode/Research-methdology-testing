from benchmark import run_benchmark

def test_determinism():

    r1 = run_benchmark(seed=42)
    r2 = run_benchmark(seed=42)

    assert r1 == r2