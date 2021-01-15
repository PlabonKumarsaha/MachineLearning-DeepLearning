import numpy as np
from numpy import random

# generates 30 random values
population = random.randint(30, size= 5)
print(population)
# sample dataset
sample = np.random.choice(population,20)
print(sample)
result_population = np.var(population)
result_sample = np.var(sample)
value =0
print(result_population)
print(result_sample)

if(result_population > result_sample):
 value =(result_sample/result_population)*100
else:
 value =(result_population/result_sample)*100

print(value )





