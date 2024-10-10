def prime(n):
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    else:
        i=5
        while i*i<=n:
            if n%i==0 or n%(i+2)==0:
                return False
            else:
                i+=6
    return True

n=int(input())
for i in range(int(n/2),n):
    if prime(i) and prime(n-i):
        print(i*(n-i))
        break