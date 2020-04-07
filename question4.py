from test import test

def sum_till_even(numbers):
    sum = 0
    for element in numbers:
        if element%2!=0:
            sum += element
        else:
            break
    return sum

def test_suite():
    test(sum_till_even([1, 3, 5, 8, 12 , 7]) == 9)
    test(sum_till_even([1, 3, 5, 7]) == 16)
    test(sum_till_even([1]) == 1)
    test(sum_till_even([]) == 0)
    test(sum_till_even([2]) == 0)

test_suite()
