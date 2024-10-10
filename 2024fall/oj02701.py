import math
def unrelated_to_seven(n):
    a=math.floor(n/10)
    b=n-10*a
    if n%7!=0 and a!=7 and b!=7:
        return True
    else:
        return False

a=int(input())
numbers=[]
i=1
while i<=a:
    if unrelated_to_seven(i):
        numbers.append(i)
    i+=1
sum=0
for number in numbers:
    sum=sum+number*number
print(sum)