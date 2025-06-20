N,K=map(int,input().split())
a=[]
for _ in range(N):
    a.append(int(input()))
if K>(sum(a)):
    print(0)
else:
    low, high = 1, int(sum(a) / K)
    max_len=0
    while low <= high:
        current=(low+high)//2
        count = 0
        for length in a:
            count += length // current
            if count>=K:
                break
        if count >= K:
            max_len=current
            low = current+1
        else:
            high = current-1
    print(max_len)