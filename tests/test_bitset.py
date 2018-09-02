import probabilistic as p
import nose.tools as nt

def test_basic():
    bs = p.bitset.BitSet(bits=6)
    bs[0] = 1


def test_set_value_other_than_zero_or_one():
    bs = p.bitset.BitSet(bits=6)

    with nt.assert_raises(ValueError):
        bs[0] = 2
