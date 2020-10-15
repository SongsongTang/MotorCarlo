import numpy as np
import time

start_time = time.time()
# set throw times
n = 100000
# throw two dice a, b
a = np.random.randint(1, 7, n)
b = np.random.randint(1, 7, n)
# sum of two dice is greater than 6
condition_1 = a + b > 6
# a > b
condition_2 = a > b
# combine the two conditions
condition = condition_1 * condition_2
# calculate the number satisfied the condition
m = sum(condition)
# calculate the probability
p = m / n
sigma = np.sqrt(p - p ** 2)
delta = 2 * sigma / np.sqrt(n)
end_time = time.time()
print("投掷" + str(n) + "次，用时" + str(round((end_time - start_time), 5)) + "s" + "\n计算值为：" + str(p) + "\n与理论值0.25的误差为：" + str(delta))
