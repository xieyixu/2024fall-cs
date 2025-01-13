n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
s=0
i=0
while i<n:
    s+=a[i]
    if s>sum(a)-s:
        break
    i+=1
print(i+1)