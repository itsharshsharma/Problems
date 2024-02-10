bird = [1,4,4,4,5,3,3,3,1,1]

def birds(x):
    x = sorted(x)
    temp = [[],[]]
    for i in x:
        if i not in temp[0]:
            temp[0].append(i)
            temp[1].append(x.count(i))
    answer = temp[0][temp[1].index(max(temp[1]))]
    print(answer)

birds(bird)