squares, day, month = [3], 3, 1
def chocolate():
    answer = 0
    temp = []
    for i in range(0,len(squares)-(month-1)):
        temp.append(squares[i:i+month])

    for j in temp:
        if sum(j) == day:
            answer += 1
    
    print(answer)
        

chocolate()
