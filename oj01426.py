from collections import deque
while True:
    n=int(input())
    if n==0:
        break
    q='1'
    queue=deque([q])
    ans=0
    while queue:
        x=queue.popleft()
        if int(x)%n==0:
            ans=int(x)
            break
        x1=x+'0'
        x2=x+'1'
        queue.append(x1)
        queue.append(x2)
    print(ans)