n=int(input())
x=n
while x>1:
    if x%2==0:
        y=x
        x=x//2
        print("{}/2={}".format(y,x))
    else:
        y=x
        x=3*x+1
        print("{}*3+1={}".format(y,x))