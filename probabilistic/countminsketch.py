import numpy
import numpy.random

# http://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/
class CountMinSketch(object):
    def __init__(self):
        self.count = 0
        self.d = 23
        self.w = 23
        self.prime = 104729
        self.a = numpy.random.random_integers(0, self.prime, self.d)
        self.b = numpy.random.random_integers(0, self.prime, self.d)
        self.estimators = numpy.empty((self.d, self.w), int)
        self.estimators.fill(0)

    def hash(self, value_hash, i):
        pos = (self.a[i] * value_hash + self.b[i]) % self.prime
        return pos % self.w

    def add(self, value):
        value_hash = hash(value)
        for i in xrange(self.d):
            self.estimators[i, self.hash(value_hash, i)] += 1
        self.count += 1

    __iadd__ = add

    def add_list(self, values):
        for value in values:
            self.add(value)

    def estimate_frequency(self, value):
        estimates = []
        value_hash = hash(value)
        for i in xrange(self.d):
            estimates.append(self.estimators[i, self.hash(value_hash, i)])

        return min(estimates)

    def max_estimation_error(self):
        return 2 * self.count / self.w

class CountMeanMinSketch(CountMinSketch):
    def __init__(self):
        CountMinSketch.__init__(self)

    def estimate_frequency(self, value):
        value_hash = hash(value)
        estimates = numpy.empty((self.d,), float)
        estimates.fill(0.0)
        for i in xrange(self.d):
            sketch_counter = self.estimators[i, self.hash(value_hash, i)]
            noise_estimation = (self.count - sketch_counter) / float(self.w - 1.0)
            estimates[i] = sketch_counter - noise_estimation

        return numpy.median(estimates)
