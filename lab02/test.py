def square(x):
    return x*x

def scale(f,x,k):
    return k*f(x)

def multiply_by(m):
    def multiply(n):
        return n*m
    return multiply

lambda x: x*x
square = lambda x : x*x
square(3)


def curry_add(x):
    def add2(y):
        return x+y
    return add2

