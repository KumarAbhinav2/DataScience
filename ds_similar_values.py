'''
Here I have an array 'a' which have several values .
Among those values , which are very near to each other ,
I want to make an array , which will contain the mean values of those nearby values .
'''


import numpy as np

a = np.array([20.0, 20.2, 20.1, 32.0, 32.0, 40.0, 40.2, 40.3])

print(np.diff(a))    # calculates diff of adjacent values
print(np.split(a, np.where(np.diff(a)>=0.5)[0]+1)) # splitting based on diff > 0.5(considering the nearness threshold (modifiable))
# and including the one at split points

my_mean = lambda a: np.sum(a)/len(a)  # mean calculation
b = np.split(a, np.where(np.diff(a)>=0.5)[0]+1)
print([my_mean(arr) for arr in b])


