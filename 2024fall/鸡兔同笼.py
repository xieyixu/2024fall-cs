a=int(input("please input the number of feet:"))
if a%4==0:
    b=int(a/4)
    c=int(a/2)
    print(b," ",c)
elif a%2==0:
    b=int((a-2)/4+1)
    c=int(a/2)
    print(b," ",c)
else:
    b=int(0)
    c=int(0)
    print(b," ",c)