from collections import Counter
n_num = [1,2,3,4,5]
n = len(n_num)
n_num.sort()


get_sum = sum(n_num)
mean = get_sum / n
print("Mean / Average is: " + str(mean))
  
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))

data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)

import math

>>> # We relay on our previous implementation for the variance
>>> def variance(data, ddof=0):
...     n = len(data)
...     mean = sum(data) / n
...     return sum((x - mean) ** 2 for x in data) / (n - ddof)
...

>>> def stdev(data):
...     var = variance(data)
...     std_dev = math.sqrt(var)
...     return std_dev
