n=int(input())
b=[]
a=list(map(int,input().split()))
b=[i for i in a if i>n]
a=[i for i in a if i<=n]

i=1
while i<=n:
    if i not in a:
        print(i,end=' ')
    i+=1
print()
b.sort()
for number in b:
    print(number,end=' ')