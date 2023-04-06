from stats_utils import *
from conf_interval import data_confidence_interval
from scipy.stats import ttest_rel


def get_paired_samples_t_test_stats(sample1, sample2):
    N = len(sample1)
    assert N == len(sample2)

    differences = [sample1[i] - sample2[i] for i in range(N)]
    mean_diff = mean(differences)
    stdDev_diff = std_dev(differences, False)
    df = N - 1
    conf_interval = data_confidence_interval(.95, differences)
    tStat, twoTailProb = ttest_rel(sample1, sample2)

    return differences, mean_diff, stdDev_diff, df, conf_interval, tStat, twoTailProb


def print_stats(sample_one, sample_two):
    differences, mean_diff, stdDev_diff, df, conf_interval, tStat, twoTailProb = get_paired_samples_t_test_stats(
        sample_one, sample_two)
    print(f'Differences: {differences}')
    print(f'Mean: {mean_diff}\tStDev: {stdDev_diff}\tdf: {df}\tConf Interval: {conf_interval}')
    print(f'T-Stat: {tStat}\tTwoTailedProb: {twoTailProb}')


if __name__ == '__main__':
    # Data from table 9.2 Intro to BioStats Ch. 9
    x = [23.5, 22.3, 20.2, 22.5, 21.3, 23.2, 23.7, 22.7, 20.2, 20.9, 22.3, 23.1, 20.3, 25.1, 24.8, 22, 21.3, 23.2, 21.3,
         22]
    y = [19.5, 20.1, 19.1, 19.2, 21.2, 19.6, 19.8, 20.2, 17.7, 18.6, 20.8, 21.1, 18.5, 16.1, 17.3, 22.4, 21.5, 18.6,
         20.5, 20.4]
    print_stats(x, y)
