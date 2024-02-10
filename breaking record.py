scores = [10,5,20,20,4,5,2,25,1]
def breakrecord():
    impr = [[],[]]
    temp = [scores[0]]
    for i in range(1,len(scores)):
        if scores[i] > max(temp):
            impr[0].append(1)
        elif scores[i] < min(temp):
            impr[1].append(1)
        temp.append(scores[i])
    temp.append(sum(impr[0]))
    temp.append(sum(impr[1]))
    print(temp[-2:])
breakrecord()