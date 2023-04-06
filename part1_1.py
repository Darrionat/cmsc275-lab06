from stats_utils import *


def get_mean_N_stdDev(sample):
    """
    Displays the mean, size, and standard deviation of a given sample
    :param sample: The dataset to check
    :return A tuple of (mean, N, stdev)
    """
    return mean(sample), len(sample), std_dev(sample, False)


def print_mean_N_stdDev(sample_one, sample_two):
    mean_1, n_1, stdev_1 = get_mean_N_stdDev(sample_one)
    mean_2, n_2, stdev_2 = get_mean_N_stdDev(sample_two)
    print(f'Sample One: {sample_one}')
    print(f'N={n_1}, Mean={mean_1}, StDev={stdev_1}')
    print(f'Sample Two: {sample_two}')
    print(f'N={n_2}, Mean={mean_2}, StDev={stdev_2}')


if __name__ == '__main__':
    prozac_group = [64, 68, 84, 65, 50, 60, 81, 76]
    truzac_group = [53, 44, 61, 50, 40, 39, 58, 42]
    print_mean_N_stdDev(prozac_group, truzac_group)
