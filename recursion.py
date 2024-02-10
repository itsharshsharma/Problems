def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

#print(factorial(5))


def digitsum(x):
    sum=0
    for i in range(len(str(x))):
        sum += int(str(x)[i])

    return sum

print(digitsum(1))