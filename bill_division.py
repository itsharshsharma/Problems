n, k = 4, 0
b, c = [3,10,2,9], 12

def charged():
    b.pop(k)
    answer = int((sum(b))/2) - c
    if answer == 0:
        print("BonAppetit")
    else:
        print(abs(answer))

charged()