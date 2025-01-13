def split(n,m,memo):
    if (n,m) in memo:
        return memo[(n,m)]
    if n==m:
        return True
    elif n<m:
        return False
    elif n%3!=0:
        return False

    result=split(n//3,m,memo) or split((n//3)*2,m,memo)
    memo[(n,m)]=result
    return result

T=int(input())
find=True
results=[]
memo={}
for _ in range(T):
    n,m=map(int,input().split())
    find=split(n,m,memo)
    results.append(find)
for result in results:
    if result:
        print('Yes')
    else:
        print('No')   #虽然题目是dp，但是我还是拿递归过了。