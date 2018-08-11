import itertools

import matplotlib.pyplot as pyplot

import numpy
import numpy.random

import countminsketch

if __name__ == '__main__':
    cm = countminsketch.CountMinSketch()
    cm.add_list(itertools.repeat(23, 100))
    cm.add_list(itertools.repeat(24, 99))
    print cm.estimate_frequency(23), cm.estimate_frequency(24)

    for i in xrange(1000):
        f = cm.estimate_frequency(i)
        if f > 0:
            print i, f

    x = numpy.arange(0, 100)
    z = numpy.random.zipf(2, 100)
    z.sort()
    z = z[::-1]
    pyplot.plot(x, z, 'ko', linewidth=2.0)
    pyplot.title('Zipf')
    pyplot.grid(True)
    pyplot.show()
