n=int(input())
numbers=list(map(int,input().split()))
s=0
t=0
for i in range(n):
    if s>0:
        if numbers[i]<0:
            s=s+numbers[i]
        else:
            s=s+numbers[i]
    elif s<=0:
        if numbers[i]>0:
            s=s+numbers[i]
        else:
            s=s
            t=t+1
print(t)