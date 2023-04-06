from stats_utils import *
from conf_interval import data_confidence_interval
from scipy.stats import ttest_ind


def get_ind_samples_t_test_stats(sample1, sample2):
    N = len(sample1)
    assert N == len(sample2)

    differences = [sample1[i] - sample2[i] for i in range(N)]
    mean_diff = mean(differences)
    stdDev_diff = std_dev(differences, False)
    df = N - 1
    conf_interval = data_confidence_interval(.95, differences)
    tStat, twoTailProb = ttest_ind(sample1, sample2)

    return differences, mean_diff, stdDev_diff, df, conf_interval, tStat, twoTailProb


def print_stats(sample_one, sample_two):
    differences, mean_diff, stdDev_diff, df, conf_interval, tStat, twoTailProb = get_ind_samples_t_test_stats(
        sample_one, sample_two)
    print(f'Differences: {differences}')
    print(f'Mean: {mean_diff}\tStDev: {stdDev_diff}\tdf: {df}\tConf Interval: {conf_interval}')
    print(f'T-Stat: {tStat}\tTwoTailedProb: {twoTailProb}')


if __name__ == '__main__':
    prozac_group = [64, 68, 84, 65, 50, 60, 81, 76]
    truzac_group = [53, 44, 61, 50, 40, 39, 58, 42]
    print_stats(prozac_group, truzac_group)
