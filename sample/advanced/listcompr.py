#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#运用列表生成器 for in if
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
print(L1)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
