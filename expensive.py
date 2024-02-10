key, mou = [13,12],[15,12,18]
b = 10

def getMoneySpent(keyboard, drives, b):

    temp = []
    for i in keyboard:
        for j in drives:
            if i+j <= b:
                temp.append(i+j)
    try:
        result = min(temp, key = lambda x: abs(x - b))
        return result
    except:
        return -1

print(getMoneySpent(key,mou,b))
