def order(a):
    n=len(a)
    if n == 1:
        return 1
    elif n == 2:
        if a[0] != a[1]:
            return 2
        else:
            return 1
    count=1
    m=0
    for i in range(1,n):
        diff=a[i]-a[i-1]
        if diff>0 and m<=0:
            m=1
            count+=1
        elif diff<0 and m>=0:
            m=-1
            count+=1
        else:
            continue
    return count
n=int(input())
a=list(map(int,input().split()))
result=order(a)
print(result)