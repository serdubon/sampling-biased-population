# pylint: disable=invalid-name
import numpy as np

# Get an array of random weight, using the mean, standard deviation
# and the probability of the person goes to the gym
def biased_population(total, mean, sd, probability, type_population="student"):
    if type_population == "student":
        return np.random.normal(mean, sd, int(total * (1 - (probability / 100))),)
    else:
        return np.random.normal(mean, sd, int(total * (probability / 100)),)


# Return a array of random select people of a population
def distribution(number_sample, sample_size, population):
    mean_distribution = []
    counter = 0
    while counter < number_sample:
        random_selection = np.random.choice(population, sample_size)
        mean_distribution.append(np.mean(random_selection))
        counter += 1
    return mean_distribution
