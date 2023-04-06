import math

import stats_utils
from scipy.stats import t


def confidence_interval(confidence, mu, stdev, N):
    dx = confidence * stdev / math.sqrt(N)
    ci = (mu - dx, mu + dx)
    return ci


def data_confidence_interval(confidence, data):
    mu = stats_utils.mean(data)
    # Population = False, so do sample stdev
    stdev = stats_utils.std_dev(data, False)
    dx = confidence * stdev / math.sqrt(len(data))
    return confidence_interval(confidence, mu, stdev, len(data))
