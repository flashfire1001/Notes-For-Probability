import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, binom

# 设置泊松分布的参数
lambda_poisson = 5

# 设置二项分布的参数，使得 np = λ
n_values = [20, 100]  # 选取较大的 n
p_values = [lambda_poisson / n for n in n_values]  # 计算 p = λ / n

# 取 k 逼近 n 的范围修改为 50 到 100
k_range_narrow = np.arange(20, 101)

# 计算泊松分布的 PMF
poisson_pmf = poisson.pmf(np.arange(0, 20), lambda_poisson)
poisson_pmf_narrow = poisson.pmf(k_range_narrow, lambda_poisson)

# 创建图像
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 颜色和 marker 形状设置
poisson_color = 'b'  # 蓝色
binomial_colors = ['r', 'g']  # 红色, 绿色
binomial_markers = ['^', 'd']  # 三角形, 菱形

# **图1：全局范围的泊松 vs. 二项分布（对数坐标）**
stem_poisson = axes[0].stem(np.arange(0, 20), poisson_pmf, linefmt=f"{poisson_color}-", markerfmt=f"{poisson_color}o", basefmt=" ", label="Poisson(λ=5)")
stem_poisson[0].set_color(poisson_color)  # 线条颜色
stem_poisson[0].set_markersize(8)  # 调整泊松分布 marker 大小

for i, n in enumerate(n_values):
    binomial_pmf = binom.pmf(np.arange(0, 20), n, p_values[i])
    stem_binomial = axes[0].stem(np.arange(0, 20), binomial_pmf, linefmt=f"{binomial_colors[i]}-",
                                 markerfmt=f"{binomial_colors[i]}{binomial_markers[i]}", basefmt=" ",
                                 label=f"Binomial(n={n}, p={p_values[i]:.3f})")
    stem_binomial[0].set_color(binomial_colors[i])  # 设置线条颜色
    stem_binomial[0].set_markersize(8)  # 调整 marker 大小

axes[0].set_xlabel("Number of Events (k)")
axes[0].set_ylabel("PMF")
# axes[0].set_yscale("log")  # **设置 y 轴为对数坐标**
axes[0].set_title("Comparison of Poisson and Binomial Distributions")
axes[0].legend()
axes[0].grid(alpha=0.3)

# **图2：仅显示 k ∈ [50, 100] 时的对比（对数坐标）**
stem_poisson_narrow = axes[1].stem(k_range_narrow, poisson_pmf_narrow, linefmt=f"{poisson_color}-", markerfmt=f"{poisson_color}o", basefmt=" ", label="Poisson(λ=5)")
stem_poisson_narrow[0].set_color(poisson_color)  # 设置线条颜色
stem_poisson_narrow[0].set_markersize(8)  # 调整泊松 marker 大小

for i, n in enumerate(n_values):
    binomial_pmf_narrow = binom.pmf(k_range_narrow, n, p_values[i])
    stem_binomial_narrow = axes[1].stem(k_range_narrow, binomial_pmf_narrow, linefmt=f"{binomial_colors[i]}-",
                                        markerfmt=f"{binomial_colors[i]}{binomial_markers[i]}", basefmt=" ",
                                        label=f"Binomial(n={n}, p={p_values[i]:.3f})")
    stem_binomial_narrow[0].set_color(binomial_colors[i])  # 设置线条颜色
    stem_binomial_narrow[0].set_markersize(8)  # 调整 marker 大小

axes[1].set_xlabel("Number of Events (k)")
axes[1].set_ylabel("PMF (log scale)")
axes[1].set_yscale("log")  # **设置 y 轴为对数坐标**
axes[1].set_title("Zoomed-in View: Binomial vs. Poisson (k = 50 to 100, log scale)")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()