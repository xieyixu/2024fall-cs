from collections import deque
A,B,C=map(int,input().split())
def bfs(A,B,C):
    initial_state=(0,0)
    queue=deque([(initial_state,[])])
    visited=set([initial_state])
    while queue:
        (x,y),operations=queue.popleft()
        if x==C or y==C:
            return operations
        possible_operations=[
            ((A,y),operations+['FILL(1)']),
            ((x,B),operations+['FILL(2)']),
            ((0,y),operations+['DROP(1)']),
            ((x,0),operations+['DROP(2)']),
            ((max(0,x-B+y),min(B,x+y)),operations+['POUR(1,2)']),
            ((min(A,x+y),max(0,y-A+x)),operations+['POUR(2,1)'])
        ]
        for new_state,new_operations in possible_operations:
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state,new_operations))
    return ['impossible']
result=bfs(A,B,C)
if result!=['impossible']:
    print(len(result))
for op in result:
    print(op)