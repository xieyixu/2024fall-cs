n=int(input())
s=input()
a=len(s)
k=a//n
answer=[]
for i in range(n):
    for j in range(k):
        if j%2==0:
            answer.append(s[j*n+i])
        else:
            answer.append(s[(j+1)*n-i-1])
print(''.join(answer))