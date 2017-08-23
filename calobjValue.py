# 0.0 coding:utf-8 0.0
# 解码并计算值

import math
from function import main_fun

def decodechrom(pop, chrom_length):   #把二进制转化为十进制
    temp = []
    for i in range(len(pop)):
        t = 0
        for j in range(chrom_length):
            t += pop[i][j] * (math.pow(2, j))
        temp.append(t)
    return temp


def calobjValue(pop, chrom_length, max_value,x_):
    temp1 = []
    obj_value = []
    temp1 = decodechrom(pop, chrom_length)
    for i in range(len(temp1)):
        x = x_+temp1[i] * max_value / (math.pow(2, chrom_length) - 1)   #这个语句规定了x的取值在【0,10】
        obj_value.append(main_fun(x))
    return obj_value

#10 * math.sin(5 * x) + 7 * math.cos(4 * x)

if __name__ == '__main__':
    pass
