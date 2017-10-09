import pandas as pd
import numpy as np
from matplotlib import pyplot, mlab

import math

a = pd.read_csv('scldata.csv')
# print a
# a.plot.show()

mu = a.mean()
print mu
# variance = 1
# sigma = math.sqrt(variance)
# x = np.linspace(mu-3*variance,mu+3*variance, 100)
# pyplot.plot(x,mlab.normpdf(x, mu, sigma))

# pyplot.show()