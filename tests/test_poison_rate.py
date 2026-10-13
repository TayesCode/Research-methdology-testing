from benchmark import run_benchmark

def test_poison_rate():

    result = run_benchmark()

    rate = result["poisons"] / result["size"]

    assert rate == 0.05