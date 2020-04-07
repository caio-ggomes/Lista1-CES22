from test import test
import math

def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n == 1:
        return False
    aux = 3
    while aux <= math.sqrt(n) + 1:
        if(n%aux==0):
            return False
        aux += 2
    return True

def test_suite():
    test(is_prime(2))
    test(is_prime(3))
    test(not is_prime(1))
    test(not is_prime(35))
    test(is_prime(11))
    test(is_prime(19911121))
    test(not is_prime(20092000))

test_suite()