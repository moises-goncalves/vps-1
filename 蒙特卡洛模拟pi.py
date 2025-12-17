# import random
#
# def approximate_pi(total_nums):
#     n_inside = 0
#     for i in range(total_nums):
#         x = random.uniform(0, 1)
#         y = random.uniform(0,1)
#
#         if x ** 2 + y ** 2 <= 1:
#             n_inside += 1
#
#     pi_approximation = 4 * n_inside / total_nums
#     return pi_approximation
#
# total_nums = 100000000
# pi_approximation = approximate_pi(total_nums)
# print(pi_approximation)

"""                                优化版                 """
# import numpy as np
#
# def approximate_pi_numpy(N_total):
#     # 1. 一次性生成所有随机点
#     x = np.random.uniform(0, 1, N_total)
#     y = np.random.uniform(0, 1, N_total)
#
#     # 2. 矢量化计算距离的平方
#     distance_squared = x**2 + y**2
#
#     # 3. 矢量化比较，并计算落在圆内的点的数量
#     N_inside = np.sum(distance_squared <= 1)
#
#     # 4. 计算pi的近似值
#     pi_approximation = 4 * (N_inside / N_total)
#     return pi_approximation
#
# # 示例：撒100万个点
# num_points = 100000000
# estimated_pi_numpy = approximate_pi_numpy(num_points)
# print(f"用 NumPy 和 {num_points} 个点模拟得到的 pi 近似值为: {estimated_pi_numpy}")



import random
import numba

@numba.njit # 或者 @numba.jit(nopython=True)
def approximate_pi_numba(N_total):
    N_inside = 0
    for _ in range(N_total): # Numba 很擅长优化这种显式循环！
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            N_inside += 1
    pi_approximation = 4 * (N_inside / N_total)
    return pi_approximation

# 示例
num_points = 100000000 # 试试更大的数，比如10^8或10^9
estimated_pi_numba = approximate_pi_numba(num_points)
print(f"用 Numba 和 {num_points} 个点模拟得到的 pi 近似值为: {estimated_pi_numba}")