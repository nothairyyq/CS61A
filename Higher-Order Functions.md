# Higher-Order Functions

## Iteration_Fibonacci Sequence

```python
def fib(n):
    prev, curn = 0,1
    k = 1
    while k < n:
        prev, curn = curn, prev+curn
        k+=1
    return curn
```

## Describing Functions

- A function's domain is the set of all inputs it might  possibly take as arguments. 
- A function's range is the set of output values it might  possibly return. 
- A pure function's behavior is the relationship it  creates between input and output.

## Generalization

```python
def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r*r*shape_constant

def area_square(r):
    #assert r > 0, 'A length must be positive'
    return area(r, 1)

def area_circle(r):
    #assert r > 0, 'A length must be positive'
    return area(r, pi)

def area_hexagon(r):
    #assert r > 0, 'A length must be positive'
    return area(r, 3*sqrt(3)/2)
```



## High Order Functions

```python
def sum_naturals(n):
    """Sum the first N natural numbers

    >>> sum_naturals(5)
    15
    """
    total, k = 0,1
    while k <= n:
        total, k = total+k, k+1
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers

    >>> sum_cubes(5)
    225
    """
    total, k = 0,1
    while k <= n:
        total, k = total+pow(k, 3), k+1
    return total

def identity(k):
    return k
def cube(k):
    return pow(k, 3)
def pi_term(k):
    return 8 / mul(4*k-3,4*k-1)
def summation(n, term):
    """
    >>> summation(5,identity)
    15
    >>> summation(5,cube)
    225
    """
    total, k =0,1
    while k <= n:
        total, k = total+term(k) , k+1
    return total
```

## Functions as Return Values

Functions defined within other function bodies are bound to names in a local frame

```python
def add_two(n):
    def adder(k):
        return n+k
    return adder
```

## The Purpose of High-Order Functions

- Functions are first-class: Functions can be manipulated as values in our programming language
- Higher-order function: A function that takes a function as an argument value or returns a function as a return value

Higher-order function:

- Express general methods of computation
- Remove repetition from programs
- Separate concerns among functions