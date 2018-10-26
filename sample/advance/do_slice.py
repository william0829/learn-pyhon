#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#用切片方法去掉文字前后空格
def trim(s):
	if s[0:1] == ' ' :
		s=s[1:]
		return trim(s)
	elif s[-2:-1] == ' ':
		s=s[:-2]
		return trim(s)
	else:
		return s 
# 测试:
if trim('hello  ') != 'hello':
	print('测试失败1!')
elif trim('  hello') != 'hello':
	print('测试失败2!')
elif trim('  hello  ') != 'hello':
	print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
	print('测试失败4!')
elif trim('') != '':
	print('测试失败5!')
elif trim('    ') != '':
	print('测试失败6!')
else:
	print('测试成功7!')

#切片使用
L = ['Michael','Sarah','Tracy','Bob','Jack']
r=[]
n=3
for i in range(n):
	r.append(L[i])
print(r)
print(L[-1:])
