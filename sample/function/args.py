#!/usr/bin/enc python3
#-*- coding utf-8 -*-
#函数参数，有必选参数、默认参数、位置参数、可变参数、命名关键字参数、关键字产生；
#必选参数必须填，默认参数可不填，参数正常按位置配；
#可变参数前面加'*'，关键字参数用dict，前面加'**'，命名关键字参数必须在可变参数后，无可变参数需在前面加'*,'


#关键字参数
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

#命名关键字参数
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)

def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')

#调用所有参数案例
def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
f2(*args,**kw)


print('打印学生资料')
def enroll(name,gender,age=6,city='Bejing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city',city)
enroll('Sarah','F')
enroll('Bob','F',7)
enroll('Adam','M',city='Tianjin')


print('打印n的x次方结果')
def power(x,n=2):
	s = 1
	while n >= 1:
		s = s * x
		n = n - 1
	return s
print(power(5,2))
print(power(5,3))
print(power(5))

