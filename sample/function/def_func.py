#!/usr/bin/enc python3
#-*- coding utf-8 -*-

#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
#的两个解。

import math
def quadratic(a,b,c):
	x = [a,b,c]
	for num in x:
		if not isinstance(num,(int,float)):
			raise TypeError('bad operand type')
	der = b*b-4*a*c
	if der > 0:
		print('此方程有两个实数解')
		n1 = (-b+math.sqrt(der))/2/a
		n2 = (-b-math.sqrt(der))/2/a
		return n1,n2
	elif der == 0:
		print('此方程只有一个实数解')
		n = -b/2/a
		return n
	elif der < 0:
		print('此方程无实数解')
		return '无解'
# 测试:
print('计算一元方程：ax^2+bx+c=0')
n = input('a = ')
a = float(n)
n = input('b = ')
b = float(n)
n = input('c = ')
c = float(n)
print(' x 为:', quadratic(a,b,c))

