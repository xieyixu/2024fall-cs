import heapq
n=int(input())
heap=[]
d=[]
ans=0
for _ in range(2*n):
    s=list(input().split())
    if s[0]=='add':
        heapq.heappush(heap,int(s[1]))
        d.append(int(s[1]))
    elif s[0]=='remove':
        x=heapq.heappop(heap)
        if x==d[-1]:
            d.pop()
        else:
            ans+=1
            d.sort(reverse=True)
            d.pop()
print(ans)