#!/usr/bin/env python3
# -*- coding utf-8 -*-

#打印从9,7,5,3,1每次相加值
sum=0
n=9
while n>0:
    sum=sum+n
    n=n-2
    print(sum)
exit()

#打印hello+名字
L=['Bart','Lisa','Adam']
n=0
while n<=2:
	print('Hello,',L[n])
	n=n+1
exit()

#打印n每个数，当n＞20时停止
n=1
while n<=100:
	if n>20:
		break
	print(n)
	n=n+1
print('END')
exit()

#打印n，当你被2整除是打印0，单n＞20是停止
n=0
while n<100:
	n=n+1
	if n%2==0:
		print(n%2)
		continue
	elif n>20:
		break
	print(n)
exit()
