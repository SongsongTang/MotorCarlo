# 导入numpy, time包
import numpy as np
import time

# 程序开始时间
start_time = time.time()
# 定义两线间距
a = 4
# 定义针长
l = 3
# 设置实验次数
n = 10000000
# 随机取n次x
x = np.random.random(n) * a
# 随机取n次θ
theta = np.random.random(n) * np.pi/2
# 判断相交条件,并计算次数
m = np.sum(x <= (l * np.sin(theta)))
# 计算相交概率
p = m / n
# 计算pi值
pi = 2 * l / (a * p)
# 程序结束时间
end_time = time.time()
# 显示用时
print("投掷" + str(n) + "次,用时" + str(round((end_time - start_time), 5)) + "s" + "\n计算Pi值为：" + str(pi) + "\n与理论值的相对误差为：" + str((pi - np.pi) / np.pi))

