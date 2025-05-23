import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# 参数设置
n = 100
p = 0.5
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.arange(30, 70)

# 三种分布
binom_pmf = binom.pmf(x, n, p)
poisson_pmf = poisson.pmf(x, mu)
normal_pdf = norm.pdf(x, mu, sigma)

# 绘图
plt.figure(figsize=(10, 6))

# Binomial PMF：用柱状图绘制
plt.bar(x, binom_pmf, width=0.8, color='gray', alpha=0.7, label='Binomial PMF')

# Poisson 和 Normal 分布：用曲线绘制
plt.plot(x, poisson_pmf, 'b--', label='Poisson Approximation')
plt.plot(x, normal_pdf, 'r-', label='Normal Approximation')

# 图形美化
plt.title('Binomial vs. Poisson and Normal Approximations')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
