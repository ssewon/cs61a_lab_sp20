"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda x: lambda y: func(x,y)

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def f(n):
        i = 1
        k = 0
        while i <= n:
            if condition(n, i):
                k = k + 1
            i = i + 1
        return k
    return f

def both_paths(sofar="S"):
    """
    >>> left, right = both_paths()
    S
    >>> leftleft, leftright = left()
    SL
    >>> rightleft, rightright = right()
    SR
    >>> _ = leftleft()
    SLL
    """
    def go_left(left1):
        def left():
            left2 = left1 + 'L'
            print(left2)
            return go_left(left2), go_right(left2)
        return left
    def go_right(right1):
        def right():
            right2 = right1 + 'R'
            print(right2)
            return go_left(right2), go_right(right2)
        return right
    print(sofar)
    return go_left(sofar), go_right(sofar)
