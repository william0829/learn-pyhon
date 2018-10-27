#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
	if L == []:
		return (None,None)
	else:
		mi = L[0]
		ma = L[0]
		for i in L:
			if i < mi:
				mi = i
			elif i > ma:
				ma = i
		return (mi,ma)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')
