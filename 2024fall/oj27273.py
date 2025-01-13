import math
n=int(input())
numbers=[int(input()) for _ in range(n)]
for number in numbers:
    s=((number+1)*number)/2
    i=0
    while 2**i<=number:
        s=s-2**(i+1)
        i+=1
    print(f"{math.ceil(s)}")