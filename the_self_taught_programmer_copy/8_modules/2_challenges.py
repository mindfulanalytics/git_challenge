# 1. Call a different function from the STATISTICS module.

import statistics

nums = [1, 5, 10, 20, 50, 100, 200, 300, 400, 500]

x = statistics.quantiles(nums)
print(x)

y = statistics.stdev(nums)
print(y)

# 2. Create a module named cubed with a function that take a number as a parameter, and returns the number cubed.
# Import and call the function from another module.

