import probabilistic as p


def test_basic():
    lc = p.linearcounter.LinearCounter()

    assert 0 == lc.estimate_cardinality()
