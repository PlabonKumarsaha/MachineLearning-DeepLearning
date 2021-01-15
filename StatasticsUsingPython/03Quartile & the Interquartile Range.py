# import the necessary packages
import statistics
# Quartile divides our data set into four equal division.

import numpy as np

dataset = [8,9,2,10,3,5,7,12,15]
q1= np.percentile(dataset,25) #25 beacuse q1 contains 25% of the data
q2 = np.percentile(dataset,50) # 50 beacuse q2 contains 50% of the data
q3 = np.percentile(dataset,75)# 75 beacuse q3 contains 75% of the data
print(q1) # output : 5 (median of lower half)
print(q2) # outpit : 8 (median)
print(q3) # output : 10 (medican of upper half)

interQuartileRange = q3-q1
print(interQuartileRange)





