from . import bitset

class BloomFilter:
    multipliers = (3, 5, 7, 11)

    def __init__(self, bits=16):
        self.bits = bits
        self.bitset = bitset.BitSet(self.bits)
        self.count = 0

    def add(self, value):
        hash_value = hash(value)
        for multiplier in self.multipliers:
            bit = (hash_value * multiplier) % self.bits
            self.bitset.setbit(bit)

        self.count += 1

        return self

    __iadd__ = add

    def __contains__(self, value):
        hash_value = hash(value)
        for multiplier in self.multipliers:
            bit = (hash_value * multiplier) % self.bits
            if self.bitset[bit] == 0:
                return False

        return True
