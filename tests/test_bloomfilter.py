import probabilistic as p
import nose.tools as nt

def test_addition():
    bf = p.bloomfilter.BloomFilter(bits=1024)
    bf.add(23)
    nt.assert_in(23, bf)

    bf += 24
    nt.assert_in(24, bf)
