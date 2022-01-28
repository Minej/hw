def reversed1(variable):
    res=[]
    for i in range(len(variable)-1,-1,-1):
        res.append(variable[i])
    res=''.join(res)
    return res

n = reversed1(input())
print(n)