from test import test

def sum_to_n(n):
    return (n*(n+1))/2

def test_suite():
    test(sum_to_n(10) == 55)
    test(sum_to_n(0) == 0)
    test(sum_to_n(1) == 1)
    test(sum_to_n(2) == 3)

test_suite()