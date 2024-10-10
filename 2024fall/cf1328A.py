n=int(input())
numbers=[]
for i in range(n):
    a=list(map(int,input().split()))
    numbers.append(a)
for i in range(n):
    a,b=numbers[i][0],numbers[i][1]
    if a%b!=0:
        print(b-(a%b))
    elif a%b==0:
        print(0)