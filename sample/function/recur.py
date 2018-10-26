#!/usr/bin/enc python3
#-*- coding utf-8 -*-
#利用递归函数设置汉诺塔玩法
def move(n,a,b,c):
	if n == 1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
move(5,'A','B','C')
exit()
