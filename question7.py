def sum_of_squares(numbers):
    sum = 0
    for number in numbers:
        sum += number**2
    return sum

print(sum_of_squares([2, 3, 4]))
print(sum_of_squares([]))
print(sum_of_squares([2, -3, 4]))