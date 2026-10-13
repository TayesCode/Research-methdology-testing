from latency_tracker import LatencyTracker

def test_latency():

    tracker = LatencyTracker()

    tracker.record_retrieval(
        lambda: sum(range(100))
    )

    tracker.record_defense(
        lambda: sum(range(100))
    )

    tracker.record_llm(
        lambda: sum(range(100))
    )

    assert abs(
        tracker.total
        -
        (
            tracker.retrieval
            +
            tracker.defense
            +
            tracker.llm
        )
    ) < 1e-6