x = "UDDDUDUUDDUU"

#/\
#  \    /
#   \/\/

def countingValleys(path):

    valley = 0
    altitude = [1 if path[0] == "U" else -1]
    for i in range(1,len(path)):
        if path[i] == "U":
            altitude.append(altitude[i-1]+1)
        else:
            altitude.append(altitude[i-1]-1)

    for i in range(len(altitude)):
        if altitude[i] == 0 and altitude[i-1] == -1:
            valley += 1

    return valley


print(countingValleys(x))