#这个文件为自己加进去的 函数文件。把目标函数单独列出来，并且在此文件下可以修改x的范围
# 0.0 coding:utf-8 0.0
# 函数
import math

def main_fun(x):
    '''目标函数为：-(x+2)*(x+1)*(x-3)*(x-4)'''
    return -(x+2)*(x+1)*(x-3)*(x-4)

def x_change(a,b):
    return [a,b]

# 计算2进制序列代表的数值
def b2d(b, max_value, chrom_length):
    t = 0
    for j in range(len(b)):
        t += b[j] * (math.pow(2, j))
    t =-5+ t * max_value / (math.pow(2, chrom_length) - 1)
    return t