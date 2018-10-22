import probabilistic as p
import nose.tools as nt

def test_basic():
    lc = p.linearcounter.LinearCounter()

    nt.assert_equal(0, lc.estimate_cardinality())
