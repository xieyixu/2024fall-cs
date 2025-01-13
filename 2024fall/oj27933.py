import heapq
n=int(input())
dq=[]
heap=[]
count=0
for _ in range(2*n):
    data=input().split()
    if data[0]=='add':
        dq.append(int(data[1]))
        heapq.heappush(heap,int(data[1]))
    elif data[0]=='remove':
        x=heapq.heappop(heap)
        if x!=dq[-1]:
            count+=1
            dq.sort(reverse=True)
            dq.pop()
        else:
            dq.pop()
print(count)