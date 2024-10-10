n=int(input())
numbers=list(map(int,input().split()))
k=int(input())
s=0
for i in range(n):
    for j in range(i+1,n):
        if numbers[i]+numbers[j]==k:
            s+=1
print(s)