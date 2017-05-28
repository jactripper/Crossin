#! usr/bin/env python
#! coding:utf-8
# 验证哥德巴赫猜想 -- Crossin每周一坑

def if_primeNum(num):
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True

def goldbach(num):
    if (num<3) or (num%2!=0):
        raise ValueError('Number should be an even over 3.')
    for i in range(2,num):  #不认为1也是质数
        if if_primeNum(i) and if_primeNum(num-i):
            return i, num-i

print(goldbach(98))
#(3,95)
print(goldbach(97))
#ValueError