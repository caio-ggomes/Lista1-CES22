def sum_till_even(numbers):
    sum = 0
    for element in numbers:
        if element%2!=0:
            sum += element
        else:
            break
    return sum

lista = [1, 3, 5 , 7, 10, 11]
print(sum_till_even(lista))