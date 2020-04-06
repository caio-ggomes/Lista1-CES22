print("       ", end = '')
for i in range(1, 12):
    print(f"{i: >2}  ", end = '')
print("12")
print("  :", end = '')
for i in range(50):
    print("-", end = '')
print('')
for i in range(1, 13):
    print(f"{i: >2}:  ", end = '')
    for j in range(1, 13):
        a = i*j
        print(f"{a: >4}", end = '')
    print('')