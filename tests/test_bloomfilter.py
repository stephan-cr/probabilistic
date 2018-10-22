import probabilistic as p


def test_addition():
    bf = p.bloomfilter.BloomFilter(bits=1024)
    bf.add(23)
    assert 23 in bf

    bf += 24
    assert 24 in bf
