# import the necessary packages
import statistics
import numpy as np

dataset = [1,2,4,8,1,9,12]
mean1 = np.mean(dataset)
print("Mean using numpy "+mean1)

mean2 = statistics.mean(dataset)

print("Mean using stat "+mean2)

# median

median1 = np.median(dataset)
print("median using numpy : "+median1)

median2 = statistics.median(dataset)
print("median using numpy : "+median2)

