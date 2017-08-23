# 0.0 coding:utf-8 0.0

import matplotlib.pyplot as plt
import math

from calobjValue import calobjValue
from calfitValue import calfitValue
from selection import selection
from crossover import crossover
from mutation import mutation
from best import best
from geneEncoding import geneEncoding
from function import main_fun,x_change,b2d

print(main_fun.__doc__)


x_ = x_change(-5,5)   #x的取值范围
max_value = (x_[1]-x_[0])     # 基因中允许出现的最大值
pop_size = 500		# 种群数量
chrom_length = 10		# 染色体长度
N = 200             #迭代次数
pc = 0.6			# 交配概率
pm = 0.01           # 变异概率
results = [[]]		# 存储每一代的最优解，N个二元组
fit_value = []		# 个体适应度
fit_mean = []		# 平均适应度

# pop = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1] for i in range(pop_size)]
pop = geneEncoding(pop_size, chrom_length)

for i in range(N):
	obj_value = calobjValue(pop, chrom_length, max_value,x_[0])        # 个体评价
	fit_value = calfitValue(obj_value)      # 淘汰

	best_individual, best_fit = best(pop, fit_value)		# 第一个存储最优的解, 第二个存储最优基因
	results.append([best_fit, b2d(best_individual, max_value, chrom_length)])

	selection(pop, fit_value)		# 新种群复制
	crossover(pop, pc)		# 交配
	mutation(pop, pm)       # 变异

results = results[1:]
results.sort()
print(results[-1])
print(best_individual)
print(best_fit)
print(obj_value[1])


print(results)
print("y = %f, x = %f" % (results[-1][0], results[-1][1]))

X = []
Y = []
for i in range(N):
	X.append(i)
	t = results[i][0]
	Y.append(t)

plt.plot(X, Y)

plt.show()
