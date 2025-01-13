from collections import defaultdict
import heapq
q=int(input())
lefts=[]
lefts_remove=set()
rights=[]
rights_remove=set()
count_map=defaultdict(int)
results=[]
for i  in range(q):
    data=input().split()
    action,l,r=data[0],int(data[1]),int(data[2])
    if action=='+':
        if count_map[(l,r)]==0:
            heapq.heappush(lefts,-l)
            heapq.heappush(rights,r)
        count_map[(l,r)]+=1
    elif action=='-':
        if count_map[(l,r)]==1:
            lefts_remove.add(l)
            rights_remove.add(r)
        count_map[(l,r)]-=1
    while lefts and -lefts[0] in lefts_remove:
        lefts_remove.remove(-lefts[0])
        heapq.heappop(lefts)
    while rights and rights[0] in rights_remove:
        rights_remove.remove(rights[0])
        heapq.heappop(rights)
    if lefts and rights:
        left_top=-lefts[0]
        right_top=rights[0]
        if left_top>right_top:
            results.append('Yes')
        else:
            results.append('No')
    else:
        results.append('No')
for result in results:
    print(result)