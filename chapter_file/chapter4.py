def sigma(n):
    if n > 0:
        return sigma(n - 1) + n
    else:
        return 0

###################################

def sigma(n):
    return loop(n, 0)

def loop(n, total):
    if n > 0:
        return loop(n - 1, n + total)
    else:
        return total

########################################

def sigma(n):
    def loop(n, total):
        if n > 0:
            return loop(n - 1, n + total)
        else:
            return total
    return loop(n, 0)

###########################################

def sigma(n):
    total = 0
    while n > 0:
        n, total = n - 1, n + total
    return total

############################################

##파이썬은 연속 재귀 호출은 일정 횟수 이상 하지 못하도록 막아놓았다.
##일정 횟수가 넘게 되면, RecursionError이 발생하게된다.

#############################################

def sigma(n):
    return n * (n + 1) // 2

#------------------------------------------------------------------------------------------------#

##실습 4.1
def sumrange(m, n):
    if m <= n:
        return m + sumrange(m + 1, n)
    else:
        return 0

def sumrange(m, n):
    def loop(m, total):
        if m <= n:
            return loop(m + 1, m + total)
        else:
            return total
    return loop(m, 0)

def sumrange(m, n):
    total = 0
    while m <= n:
        m, total = m + 1, m + total
    return total

#------------------------------------------------------------------------------------------------#

def power(b, n):
    if n > 0:
        return b * power(b, n - 1)
    else:
        return 1
    

def power(b, n):
    def loop(b, n, prod):
        if n > 0:
            return loop(b, n - 1, b * prod)
        else:
            return prod
    return loop(b, n, 1)

def power(b, n):
    def loop(n, prod):
        if n > 0:
            return loop(n - 1, b * prod)
        else:
            return prod
    return loop(n, 1)

##
def power(b, n):
    prod = 1
    while n > 0:
        n, prod = n - 1, b * prod
    return prod

def power(b, n):
    if n > 0:
        if n % 2 == 0:
            return power(b * b, n // 2)
        else:
            return b * power(b, n - 1)
    else:
        return 1

def power(b, n):
    def loop(b, n, prod):
        if n > 0:
            if n % 2 == 0:
                return loop(b * b, n // 2, prod)
            else:
                return loop(b, n - 1, b * prod)
        else:
            return prod
    return loop(b, n, 1)

def power(b, n):
    prod = 1
    while n > 0:
        if n % 2 == 0:
            b, n = b * b, n // 2
        else:
            n, prod = n - 1, b * prod
    return prod

#------------------------------------------------------------------------------------------------#

##최대공약수

from math import gcd
from selectors import EpollSelector
print(gcd(48, 18))
print(gcd(18, 48))

def gcd(m, n):
    if n != 0:
        return gcd(n, m % n)
    else:
        return m

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

#------------------------------------------------------------------------------------------------#

##최소공배수 - Divide and Conquer

def even(n):
    return n % 2 == 0

def odd(n):
    return n % 2 == 1

def gcd(m, n):
    if not (m == 0 or n == 0):
        if even(m) and even(n):
            return 2 * gcd(m // 2, n // 2)
        elif even(m) and odd(m):
            return gcd(m // 2, n)
        elif odd(m) and even(n):
            return gcd(m, n // 2)
        else:
            return gcd(n, (m - 2) // 2)
    else:
        if m == 0:
            return n
        else:
            return m

def gcd(m, n):
    def loop(m, n, k):
        if not (m == 0 or n == 0):
            if even(m) and even(n):
                return loop(m // 2, n // 2, 2 * k)
            elif even(m) and odd(m):
                return loop(m // 2, n, k)
            elif odd(m) and even(n):
                return loop(m, n // 2, k)
            elif m <= n:
                return loop(m, (n - m) // 2, k)
            else:
                return loop(n, (m - n) // 2, k)
        else:
            if m == 0:
                return n * k
            else:
                return m * k
            
def gcd(m, n):
    k = 1
    while not (m == 0 or n == 0):
        if even(m) and even(n):
            m, n, k = m // 2, n // 2, 2 * k
        elif even(m) and odd(n):
            m = m // 2
        elif odd(m) and even(n):
            n = n // 2
        elif m <= n:
            n = (n - m) // 2
        else:
            m, n = n, (m - n) // 2
    if m == 0:
        return n * k
    else:
        return m * k

#------------------------------------------------------------------------------------------------#

##곱셈 part 1.

def mult(m, n):
    if n > 0:
        return m + mult(m, n - 1)
    else:
        return 0

def mult(m, n):
    def loop(n, total):
        if n > 0:
            return loop(n - 1, m + total)
        else:
            return 0
    return loop(n, 0)

def mult(m, n):
    total = 0
    while n > 0:
        total, n = m + total, n - 1
    return total

##곱셈 part 2.

def fastmult(m, n):
    if n > 0:
        if n % 2 == 0:
            return fastmult(m + m, n // 2)
        else:
            return m + fastmult(m + m, n - 1)
    else:
        return 0
    
def fastmult(m, n):
    def loop(m, n, total):
        if n > 0:
            if n % 2 == 0:
                return loop(m + m, n // 2, total)
            else:
                return loop(m, n - 1, total + m)
        return total    
    return loop(m, n, 0)

def fastmult(m, n):
    total = 0
    while n > 0:
        if n % 2 == 0:
            m, n = m + m, n // 2
        else:
            total, n = m + total, n - 1
    return total

#------------------------------------------------------------------------------------------------#

##러시안 농부

def russian_mult(m, n):
    def loop(m, n):
        if n > 1:
            if n % 2 == 1:
                return m + loop(m + m, n // 2)
            else: # n == 1
                return loop(m + m, n // 2)
        else:
            return m
    if n > 0:
        return loop(m, n)
    else:
        return 0

def russian_mult(m, n):
    def loop(m, n, a):
        if n > 1:
            if n % 2 == 1:
                return loop(m + m, n // 2, m + a)
            else:
                return loop(m + m, n // 2, a)
        else:
            return a
    if n > 0:
        return loop(m, n, 0)
    else:
        return 0

def russian_mult(m, n):
    if n > 0:
        a = 0
        while n > 0:
            if n % 2 == 1:
                a += m
            m, n = m + m, n // 2
        return a
    else:
        return 0
                
    

