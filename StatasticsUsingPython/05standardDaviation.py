import numpy as np
from numpy import random

# generates 30 random values
population = random.randint(30, size= 10)
print(population)
# sample dataset
sample_std = np.random.choice(population,15)
print(sample_std)
# find the standard daviation
result_population_daiation = np.std(population)

result_sample = np.std(sample_std)

print(result_population_daiation)
print(result_sample)





