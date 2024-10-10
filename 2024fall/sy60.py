def narcissus(n):
    numbers=[int(d) for d in str(n)]
    s=sum(number**3 for number in numbers)
    if s==n:
        return True

a,b=map(int,input().split())
j=0
numbers=[]
for i in range(a,b+1):
    if narcissus(i):
        numbers.append(i)
        j+=1
if j!=0:
    print(' '.join(map(str,numbers)))
elif j==0:
    print("NO")