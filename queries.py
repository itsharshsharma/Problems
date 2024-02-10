import numpy as np
n, q = 2, 7
arr1 = [[1,0,5], [1,1,7], [1,0,3], [2,1,0], [2,1,1]]
arr2 = [[1,1,4],[2,1,1],[2,0,6],[1,0,4],[2,0,2],[1,1,8],[1,0,0]]

def bit_q(n,queries):
    output = [[],[]]
    lastAnswer = 0
    answer = []

    for i in range(q):
        idx = ((queries[i][1] ^ lastAnswer) % n)
        if queries[i][0] == 1:
            output[idx].append(queries[i][-1])
        else:
            lastAnswer = output[idx][queries[i][2] % len(output[idx])]
            output[idx].append(lastAnswer)
            answer.append(lastAnswer)

    print(answer)

bit_q(n,arr2)