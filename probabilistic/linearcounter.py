from . import bitset
import math

class LinearCounter(object):
    '''
    probabilistically count the number of distinct values
    '''

    def __init__(self, bits=16, capacity=256):
        '''
        :param bits: available space
        :param capacity: expected number of distinct values
        '''

        self.bits = bits
        self.bitset = bitset.BitSet(bits)
        self.capacity = capacity

    def add(self, value):
        pos = hash(value) % self.bits
        self.bitset.setbit(pos)

    def estimate_cardinality(self):
        '''
        estimate the number of distinct values seen so far
        '''

        card = -self.bits * math.log((self.bits - self.bitset.count_set_bits()) \
                                         / float(self.bits))
        return int(round(card))

    def estimate_bias(self):
        load_factor = self.capacity / float(self.bits)
        return (math.exp(load_factor) - load_factor - 1.0) / (2.0 * self.capacity)
