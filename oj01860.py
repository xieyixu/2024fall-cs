import sys
input=sys.stdin.read().split()
idx=0
N=int(input[idx])
idx+=1
M=int(input[idx])
idx+=1
S=int(input[idx])
idx+=1
V=float(input[idx])
idx+=1

edges=[]
for _ in range(M):
    A=int(input[idx])
    idx+=1
    B=int(input[idx])
    idx+=1
    RAB = float(input[idx])
    idx += 1
    CAB = float(input[idx])
    idx += 1
    RBA = float(input[idx])
    idx += 1
    CBA = float(input[idx])
    idx += 1
    edges.append((A,B,RAB,CAB))
    edges.append((B,A,RBA,CBA))
max_amount=[0.0]*(N+1)
max_amount[S]=V
has_cycle=False
for i in range(N):
    current=max_amount.copy()
    updated=False
    temp=current.copy()
    for edge in edges:
        A,B,rate,comn=edge
        if current[A]>comn:
            new_B=(current[A]-comn)*rate
            if new_B>temp[B]:
                temp[B]=new_B
                updated=True
    max_amount=temp
    if not updated:
        break
    if i==N-1:
        has_cycle=True
if has_cycle:
    print('YES')
else:
    print('YES' if max_amount[S]>V else 'NO')