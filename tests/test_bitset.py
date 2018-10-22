import probabilistic as p
import nose.tools as nt

def test_basic():
    bs = p.bitset.BitSet(bits=6)
    bs[0] = 1


def test_set_value_other_than_zero_or_one():
    bs = p.bitset.BitSet(bits=6)

    with nt.assert_raises(ValueError):
        bs[0] = 2


def test_count_bits_set():
    bs = p.bitset.BitSet(bits=6)

    bs[0] = 1
    bs[5] = 1

    nt.assert_equal(2, bs.count_set_bits())

    bs[0] = 0

    nt.assert_equal(1, bs.count_set_bits())
