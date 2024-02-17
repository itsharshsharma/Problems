s = ['aba','baba','aba','xzxb']
q = ['aba','xzxb','ab']

def matchingStrings(stringList, queries):
    count = 0
    result = []

    for i in queries:
        result.append(stringList.count(i))

    return result

print(matchingStrings(s,q))
