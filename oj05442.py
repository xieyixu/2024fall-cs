n=int(input())
if n==0:
    print(0)
    exit()


letters=[chr(ord('A')+i) for i in range(n)]
letter_to_index={ch:i for i,ch in enumerate(letters)}

edges=[]
for _ in range(n-1):
    parts=input().split()
    u_char=parts[0]
    k=int(parts[1])
    idx=2
    for _ in range(k):
        v_char=parts[idx]
        w=int(parts[idx+1])
        edges.append((letter_to_index[u_char],letter_to_index[v_char],w))
        idx+=2

edges.sort(key=lambda x:x[2])

parent=list(range(n))

def find(u):
    while parent[u]!=u:
        parent[u]=parent[parent[u]]
        u=parent[u]
    return u

total=0
count=0

for u,v,w in edges:
    root_u=find(u)
    root_v=find(v)
    if root_u!=root_v:
        total+=w
        parent[root_v]=root_u
        count+=1
        if count==n-1:
            break

print(total)