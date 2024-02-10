x = [[5,3,4],[1,5,8],[6,4,2]]

#5 3 4
#1 5 8
#6 4 2

y = [[4,9,2],[3,5,9],[8,1,5]]

#4 9 2
#3 5 7
#8 1 5


def magic_sq(arr):
    ans = 0

    for i in range(3):  
        if sum(arr[i]) != 15:
            ans += abs(sum(arr[i]) - 15)
    return ans

print(magic_sq(y))

