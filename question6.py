import math

def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    aux = 3
    while aux <= math.sqrt(n) + 1:
        if(n%aux==0):
            return False
        aux += 2
    return True

print(is_prime(3))
print(is_prime(5))
print(is_prime(11))
print(not is_prime(35))
print(is_prime(19911121))
print(is_prime(2))
print(is_prime(104))