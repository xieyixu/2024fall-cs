while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    ans=0
    while len(a):
        if a[-1]>b[-1]:  #田忌最快的比齐威王快，tj赢
            ans+=200
            del a[-1],b[-1]
        elif a[-1]<b[-1]: #否则使用最慢的去比
            ans-=200
            del a[0],b[-1]
        else:#如果平局
            if a[0]>b[0]: #从第一个比，避免不必要的失败
                ans+=200
                del a[0],b[0]
            else:
                if a[0]<b[-1]:
                    ans-=200
                del a[0],b[-1]
    print(ans)