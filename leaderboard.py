x = [100, 90, 90, 80]
#10,20,40,50,100
y = [70,80,105]

def leaderboard(board, score):
    
    temp = []
    for i in score:
        board.append(i)
        board = sorted(set(board), reverse = True)
        temp.append(board.index(i)+1)
        
        board.remove(i)
    
    return temp, board



result = leaderboard(x,y)

print(result)