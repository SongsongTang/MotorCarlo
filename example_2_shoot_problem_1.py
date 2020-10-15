# 导入numpy, time包
import numpy as np
import time

# 程序开始时间
start_time = time.time()
# 射击n次
n = 10000000
# 取n次随机数
r = np.random.random(n)
# 小于0.1的随机数
r1 = r <= 0.1
# 小于0.2的随机数
r2 = r <= 0.2
# 小于0.5的随机数
r5 = r <= 0.5
# 小于1的随机数
r10 = r <= 1
# 计算运动员总得分
m = sum(r1 * 7 + (r2 ^ r1) * 8 + (r5 ^ r2) * 9 + (r10 ^ r5) * 10)
# 计算运动员平均得分
gn = m / n
# 显示运动员射击成绩近似值
print("运动员射击成绩近似值：" + str(gn))
# 程序运行结束时间
end_time = time.time()
# 显示用时
print("射击" + str(n) + "次，用时" + str(end_time - start_time) + "s")
