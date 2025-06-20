def check(s):
    count,x1=0,0
    for i in range(len(s)):
        if s[i]=='@':
            count+=1
            x1=i
            if x1==0 or x1==len(s)-1:
                return False
    if count!=1:
        return False
    if s[0]=='.' or s[-1]=='.':
        return False
    count_2=0
    for i in range(x1,len(s)):
        if s[i]=='.':
            count_2+=1
            if i==x1+1:
                return False
    if s[x1-1]=='.':
        return False
    if count_2==0:
        return False
    return True
try:
    while True:
        s=input().strip()
        if check(s):
            print('YES')
        else:
            print('NO')
except EOFError:
    pass