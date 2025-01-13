def Honoi(n,x,y,z):
    if n==1:
        print(f'{x}->{z}')
    else:
        Honoi(n-1,x,z,y)
        print(f'{x}->{z}')
        Honoi(n-1,y,x,z)

n=int(input())
x='A';y='B';z='C'
print(2**n-1)
Honoi(n,x,y,z)