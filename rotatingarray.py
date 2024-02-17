import random
n,d = 5, 4
arr = [i for i in range(1,6)]

def rotateLeft(d, arr):

    rot_arr = arr.copy()
    for j in range(d):
        for i in range(-len(arr),0):
            rot_arr[i] = arr[i+1]

        arr = rot_arr.copy()

    print(rot_arr)

def anotherrotation(d,arr):
    while d > 0:
            arr.append(arr.pop(0))
            d -= 1
    return arr

anotherrotation(d,arr)