import numpy as np
n, q = 2, 5
arr1 = [[1,0,5], [1,1,7], [1,0,3], [2,1,0], [2,1,1]]
arr2 = [[1,1,4],[2,1,1],[2,0,6],[1,0,4],[2,0,2],[1,1,8],[1,0,0]]

def bit_q(n,queries):
    output = []
    for _ in range(n):
        output.append([])
    lastAnswer = 0
    answer = []

    for i in range(q):
        type, x, y = queries[i]
        if type == 1:
            idx = ((x ^ lastAnswer) % n)
            output[idx].append(y)
        elif type == 2:
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = output[idx][y % len(output[idx])]
            answer.append(lastAnswer)
            
    print(answer)

bit_q(n,arr1)