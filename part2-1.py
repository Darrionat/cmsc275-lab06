from readcsv import load_data
import random
from part1_3 import get_ind_samples_t_test_stats


def compare(sample1, sample2):
    differences, mean_diff, stdDev_diff, df, conf_interval, tStat, twoTailProb = get_ind_samples_t_test_stats(sample1,
                                                                                                              sample2)
    print('p-value', twoTailProb)


if __name__ == '__main__':
    stickleback = load_data('Sticklebacks.csv')
    bluegill = load_data('Bluegill.csv')
    mosquito = load_data('Mosquitofish.csv')
    stickleback_samples = random.sample(stickleback, 6)
    bluegill_samples = random.sample(bluegill, 6)
    mosquito_samples = random.sample(mosquito, 6)

    compare(bluegill_samples, mosquito_samples)
    compare(stickleback_samples, mosquito_samples)
