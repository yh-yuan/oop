#!usr/bin/python  
#-*- coding:utf-8 _*-

l=[x*x for x in range(5)]

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3
g=odd()
one=next(g)
print(one)
two=next(g)
print(two)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
    return 'Done'
fib(5)

def fiby(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'Done'
g=fiby(5)
for i in range(6):
    rst=next(g)
    print(rst)

