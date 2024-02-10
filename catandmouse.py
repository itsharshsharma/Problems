def catAndMouse(x, y, z):

    result = min([x,y], key = lambda a: abs(a-z))

    if result == x and abs(x - z) != abs(y-z):
        return "Cat A"
    elif result == y and abs(x - z) != abs(y-z):
        return "Cat B"
    else:
        return "Mouse C"

print(catAndMouse(10,10,10))