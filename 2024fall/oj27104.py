N=int(input())
a=list(map(int,input().split()))
r=[[i-a[i] if i-a[i]>=0 else 0,i+a[i] if i+a[i]<=N-1 else N-1] for i in range(N)]
r.sort(key=lambda x:(x[0]))
start,end=0,N-1
count=0
current_index=0
while current_index<=N-1:
    max_right=float('-inf')
    while current_index<=N-1 and r[current_index][0]<=start:
        max_right=max(max_right,r[current_index][1])
        current_index+=1
    if max_right<start:
        break
    count+=1
    if max_right>=end:
        break
    start=max_right+1
print(count)