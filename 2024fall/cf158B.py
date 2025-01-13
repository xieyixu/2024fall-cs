from math import ceil
from math import floor
from collections import Counter
n=int(input())
s=list(map(int,input().split()))
d=Counter(s)
x,y,z,w=d[1],d[2],d[3],d[4]
sum=w+floor(y/2)+min(x,z)
y=y-2*floor(y/2)
x,z=x-min(x,z),z-min(x,z)
if x==z:
    sum=sum+y
elif x==0:
    sum=sum+z-x+y
elif z==0:
    if y==0:
        sum=sum+ceil(x/4)
    elif y==1:
        sum=sum+1+ceil(max(x-2,0)/4)
print(sum)