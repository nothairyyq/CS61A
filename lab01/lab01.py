def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    smallest = n-k+1
    sum = 1
    if k == 0:
        return sum
    else:
        while n >= smallest:
            sum *= n
            n -= 1
        return sum


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    i=10
    sum=0
    if y < 10:
        return y
    elif y == 10:
        return 1
    else:
        while y > 10:
            remainder = y%i
            sum+=remainder
            y=y//i         
        return sum+y




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    i=10
    sum=0
    if n < 10:
        return False
    else:
        while n > 10:
            remainder = n%i
            if remainder == 8:
                sum += 1
            n = n // i
    
    if n == 8:
        sum+=1

    if sum == 2:
        return True
    else:
        return False