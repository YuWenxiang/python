# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]

print(L2)

#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,b+a
        n=n+1
    return 'done'

f = fib(8)
print('fib(8):',f)
print('斐波拉契数列n=8：')
for i in f:
    print(i)

#杨辉三角
def triangles():
    g = [1]
    while True:
        yield g
        g.append(0)
        g = [g[i]+g[i-1] for i in range(len(g))]

n = 0
print('杨辉三角n=10:')
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break
