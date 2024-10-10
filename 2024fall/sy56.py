n=int(input())
numbers=list(map(int,input().split()))
i=0
j=0
for i in range(n-1):
    if numbers[i]>numbers[i+1]:
        print("NO")
        j=1
        break
if j==0:
    print("YES")