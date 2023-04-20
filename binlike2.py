import numpy as np
from scipy.stats import binom

def binomial_likelihood(al, j1, j2, n):
    p = j1 / j2
    likelihood = binom.pmf(al, n, p)
    return likelihood
