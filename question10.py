from test import test

def add_complex(a, b):
    return (a[0]+b[0], a[1]+b[1])


def test_suite():
    test(add_complex((0, 0), (1, 1)) == (1, 1))
    test(add_complex((2, 3), (1, -1)) == (3, 2))
    test(add_complex((0, 1), (1, 0)) == (1, 1))
    test(add_complex((-7, -2), (1, 4)) == (-6, 2))

test_suite()