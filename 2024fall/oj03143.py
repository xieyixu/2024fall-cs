import math

def prime(n):
    if n==3:
        return True
    if n%2==0:
        return False
    if n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=2
    return True

a=int(input())

if a<6 or a%2!=0:
    print("Error!")
else:
    for x in range(3,int(a/2)+1,1):
        y=a-x
        if prime(x) and prime(y):
            print(f"{a}={x}+{y}")