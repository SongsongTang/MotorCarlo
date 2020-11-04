import numpy as np
import matplotlib.pyplot as plt

# 1.1 直接抽样
xi = np.random.rand(1000000)
x = (xi) ** (2/3)
bins = np.linspace(0, 1, 100)
y = (3/2) * bins ** (1/2)
plt.figure(u"1.1 direct sample")
plt.hist(x, bins=bins, density=True)
plt.plot(bins, y)

# 1.2 挑选抽样
# set h(x)=1, M=3/2, xh=xi**2
xi_2 = np.random.rand(1000000)
xh = xi_2 ** 2
i = xi <= xh
xh = xh[i]
plt.figure("1.2 select sample")
plt.hist(xh, bins=bins, density=True)
plt.plot(bins, y)

# 2 对称抽样
# f1 = 1/2, H = x/2
eta = 2 * xi - 1
xi_3 = np.random.rand(1000000)
j = eta <= xi_3
xi_3 = np.concatenate((xi_3[j], -xi_3[~j]))
bins = np.linspace(-1, 1, 200)
y = 1/2 * (1 + bins)
plt.figure("2 symmetry sample")
plt.hist(xi_3, bins=bins, density=True)
plt.plot(bins, y)

# 3 光子散射后能量分布抽样，令a = 1
a = 1
xi_1 = np.random.rand(1000000)
xi_2 = np.random.rand(1000000)
xi_3 = np.random.rand(1000000)
k = xi_1 <= 27 / (4 * a + 29)
xf1 = (1 + 2 * a) / (1 + 2 * a * xi_2[k])
xf2 = 1 + 2 * a * xi_2[~k]
x1 = 1 / 2 * (((a + 1 - xf1) / a) ** 2 + 1)
x2 = 27 / 4 * ((xf2 - 1) ** 2) / (xf2 ** 3)
x = np.concatenate((x1, x2))
i = xi_3 <= x
xf = np.concatenate((xf1, xf2))[i]
x = np.linspace(1, 1 + 2 * a, 300)
K = (1 - 2 * (a + 1) / a ** 2) * np.log(1 + 2 * a) + 1 / 2 + 4 / a - 1 / (2 * (2 * a + 1) ** 2)
y = 1 / K * ((((a + 1 - x) / a) ** 2 + 1 / x) * 1 / x ** 2 + (1 / x - 1 / x ** 2))
plt.figure("3")
plt.hist(xf, bins=x, density=True)
plt.plot(x, y)

# 4 复合抽样
xi_1 = np.random.rand(1000000)
xi_2 = np.random.rand(1000000)
yf2 = xi_1
i = xi_2 <= xi_1
xf = xi_2[i] * xi_1[i]
x = np.linspace(0.01, 1, 100)
y = -np.log(x)
plt.figure("4")
plt.hist(xf, bins=x, density=True)
plt.plot(x, y)

# 5 x取值范围暂取[-a, a]
a = 6
xi = np.random.rand(1000000)
eta = xi - 1 / 2
i = eta <= 0
xf1 = -np.log(-2 * eta[i])  # x > 0
xf2 = np.log(2 * eta[~i])   # x < 0
xf = np.concatenate((xf2, xf1))
x = np.linspace(-a, a, 1000)
y = 1 / 2 * np.exp(-np.abs(x))
plt.figure("5")
plt.hist(xf, bins=x, density=True)
plt.plot(x, y)

plt.show()
