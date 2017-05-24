#! usr/bin/env python
#! coding:utf-8
#! 杨辉三角--Crossin 每周一坑

def yanghui(m,n):
    if n > m+1:
        raise IndexError('n out of index')
    if m<2 or n==0 or n==m :
        return 1
    else:
        return (yanghui(m-1,n-1) + yanghui(m-1,n))

def generate_yh(m):
    layer = [1]
    for i in range(0,m):
        print(*layer)
        layer.append(0)
        layer = [(layer[i-1] + layer[i]) for i in range(len(layer))]

generate_yh(5)