arr, k = [5,4,2,6,4,2,3,2,1,5], 7

def sumpair():
    answer = 0
    s_pair = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and i < j:
                s_pair = arr[i] + arr[j]
            
                if s_pair % k == 0:
                    print(s_pair, [arr[i], arr[j]])
                    answer += 1

    print(answer)

sumpair()