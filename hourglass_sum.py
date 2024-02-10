import numpy as np
hourglass_a = [[-9, -9, -9, 1, 1, 1],[0,-9,0,4,3,2],[-9, -9, -9,  1, 2, 3],[0,  0,  8,  6, 6, 0],[0,  0,  0, -2, 0, 0],[0,  0,  1,  2, 4, 0]]

print(np.array(hourglass_a))

def hourglass(arr):
    result = []
    output = []
    for row in range(4):
        for col in range(4):
            output.extend([arr[row][col:col+3]])
            output[len(output)-1].append(arr[row+1][col+1])
            output[len(output)-1].extend(arr[row+2][col:col+3])
        
            result.append(sum(output[len(output)-1]))

    return max(result)

print(hourglass(hourglass_a))