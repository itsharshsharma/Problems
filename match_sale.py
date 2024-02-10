socks = [10, 20, 20, 10, 10, 30, 50, 10]

def match(ar):
    answer = 0
    for i in set(ar):
        if ar.count(i) / 2 >= 1:
            answer += int(ar.count(i) / 2)

    return answer

print(match(socks))