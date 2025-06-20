while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    count=0
    left=right=m
    while left<=n:
        count+=min(right,n)-left+1
        left*=2
        right=right*2+1
    print(count)