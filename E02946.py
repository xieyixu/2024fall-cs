k,N=map(int,input().split())
for _ in range(N):
    s,num=input().split()
    if s=='multiply':
        k=k*(int(num))
    if s=='plus':
        k=k+int(num)
    if s=='minus':
        k=k-int(num)
print(k)