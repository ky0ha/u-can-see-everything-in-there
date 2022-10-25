import matplotlib.pyplot as plt
import numpy as np

class fig(object):
    def __init__(self, x, y, *args, **kwargs):
        plt.plot(x, y, *args, **kwargs)
        plt.show()