import random

arr = list()

for i in range(100):
    arr.append(random.randint(i,200))


def maximum():
    max= 0
    for j in arr:
        if j > max:
            max = j
    return max



print(maximum())