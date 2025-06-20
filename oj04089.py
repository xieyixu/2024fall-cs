def check(s1,s2):
    return s2.startswith(s1)
t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(input())
    a.sort()
    find=True
    for i in range(n-1):
        if check(a[i],a[i+1]):
            find=False
    if find:
        print('YES')
    else:
        print('NO')