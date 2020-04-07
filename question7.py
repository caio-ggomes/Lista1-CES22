from test import test


def sum_of_squares(numbers):
    sum = 0
    for number in numbers:
        sum += number**2
    return sum


def test_suite():
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([2, -3, 4]) == 29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2]) == 4)
    test(sum_of_squares([0]) == 0)

test_suite()