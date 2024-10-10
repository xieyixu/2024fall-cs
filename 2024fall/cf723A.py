def compare(x,y):
    if x>y:
        return y,x
    else:
        return x,y

x,y,z=map(int,input().split())
x,y=compare(x,y)
x,z=compare(x,z)
y,z=compare(y,z)

s=z-x
print(s)