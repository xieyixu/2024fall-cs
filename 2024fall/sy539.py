def blessed_number(A):
    n=len(A)
    a=int(A)
    i=1
    square=set()
    while i*i<=a:
        square.add(str(i*i))
        i+=1
    def dfs(b):
        if not b:
            return True
        for i in range(1,len(b)+1):
            part=b[:i]
            if part in square:
                if dfs(b[i:]):
                    return True
        return False
    return dfs(A)

A=input()
if blessed_number(A):
    print('Yes')
else:
    print('No')