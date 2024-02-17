n,m = 5,3
q = [[1,2,100],[2,5,100],[3,4,100]]

def arrayManipulation(n, m, queries):

    result = [0 for _ in range(n)]

    for i in range(m):
        a,b,k = queries[i]
        result[a-1:b] = list(map(lambda x: x+k, result[a-1:b]))

    print(f"{result}\n{max(result)}")
    return max(result)

# arrayManipulation(n,m, q)

def AnotherarrayManipulation(n, queries):
    arr = [0] * (n + 1)  # Initialize the array with one extra element
    
    # Perform prefix sum
    for query in queries:
        a, b, k = query
        arr[a - 1] += k  # Add k to the start index of the range
        arr[b] -= k      # Subtract k from the index after the end of range
    
    max_val = 0
    prefix_sum = 0
    for val in arr:
        prefix_sum += val
        max_val = max(max_val, prefix_sum)
    
    return arr, max_val

print(AnotherarrayManipulation(n,q))