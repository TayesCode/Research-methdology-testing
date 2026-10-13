from benchmark import run_benchmark

def test_cost_accounting():

    result = run_benchmark()

    assert result["calls"] == 10