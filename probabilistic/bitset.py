def required_bytes(bits):
    return bits // 8 + (0 if bits % 8 == 0 else 1)

def byte_and_offset(bit):
    return (bit // 8, bit % 8)

class BitSet:
    def __init__(self, bits):
        self.bits = bits
        self.bytes = required_bytes(bits)
        self.array = bytearray(self.bytes)

    def __getitem__(self, bit):
        if bit < 0 or bit >= self.bits:
            raise IndexError('bit set out of range')

        byte, offset = byte_and_offset(bit)

        assert offset >= 0
        assert offset < 8

        return 1 if (self.array[byte] & (1 << offset)) > 0 else 0

    def __setitem__(self, bit, value):
        if bit < 0 or bit >= self.bits:
            raise IndexError('bit set out of range')

        if value not in (0, 1):
            raise ValueError('value must be 0 or 1')

        byte, offset = byte_and_offset(bit)

        if value > 0:
            self.array[byte] = self.array[byte] | (1 << offset)
        else:
            self.array[byte] = self.array[byte] & ~(1 << offset)

    def setbit(self, bit):
        self[bit] = 1

    def unsetbit(self, bit):
        self[bit] = 0

    def count_set_bits(self):
        count = 0
        for bit in range(self.bits):
            count += self[bit]

        return count
