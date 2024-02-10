year = 1800

def is_leap(x):
    if x < 1918 and x % 4 == 0:
        answer = "12.09."+str(year)
    elif x > 1918 and x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        answer = "12.09."+str(year)
    elif x == 1918:
        answer = "26.09."+str(year)
    else:
        answer = "13.09."+str(year)
        

    print(answer)

is_leap(year)
    
