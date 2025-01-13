import heapq
n=int(input())
a=list(map(int,input().split()))
count=0
sum_drink=0
min_heap=[]
for i in range(n):
    if a[i]>0:
        count+=1
        sum_drink+=a[i]
        heapq.heappush(min_heap,a[i])
    else:
        if sum_drink+a[i]>=0:
            count+=1
            sum_drink+=a[i]
            heapq.heappush(min_heap,a[i])
        elif min_heap and a[i]>min_heap[0]:
            sum_drink=sum_drink+a[i]-heapq.heappop(min_heap)
            heapq.heappush(min_heap,a[i])
print(count)