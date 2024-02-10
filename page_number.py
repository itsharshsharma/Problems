x,y = 6,6

def turn_to_page(page, to):
    trigger = True

    if page % 2 == 1:
        answer = 0
    else:
        answer = 1
    
    if page % 2 == 1 and (to == 1 or to == page or to == page - 1):
        return answer, trigger

    else:
        if page - to >= (page/2):
            answer = int(to/2)
        else:
            answer = int(page/2) - int(to/2)
        return answer, not trigger

print(turn_to_page(x,y))