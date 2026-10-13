from metrics import compute_asr

def test_metric_validation():

    asr = compute_asr(8, 10)

    assert asr == 0.8