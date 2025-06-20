n=int(input())
s=list(input())
board=[[] for _  in range(n)]
l=len(s)
k=l//n
for i in range(k):
    if i%2==0:
        for j in range(n):
            board[j].append(s[i*n+j])
    else:
        for j in range(n):
            board[j].append(s[(i+1)*n-j-1])
answer=list()
for i in range(n):
    answer+=board[i]
print(''.join(map(str,answer)))