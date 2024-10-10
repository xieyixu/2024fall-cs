import math
n=int(input())
numbers=[]
i=0
while i<n:
    a=int(input())
    numbers.append(a)
    i+=1
j=0
while j<n:
    c=math.floor(numbers[j]/1000000)
    y=math.floor((numbers[j]-c*1000000)/10000)
    m=math.floor((numbers[j]-c*1000000-y*10000)/100)
    d=numbers[j]-c*1000000-y*10000-m*100
    if m>2:
        m=m
    elif (m==1 or m==2) and y!=0:
        m=m+12
        y=y-1
    elif (m==1 or m==2) and y==0:
        m=m+12
        y=99
        c=c-1
    w=(y+math.floor(y/4)+math.floor(c/4)-2*c+math.floor((26*(m+1))/10)+d-1)%7
    if w==0:
        print("Sunday")
    if w==1:
        print("Monday")
    if w==2:
        print("Tuesday")
    if w==3:
        print("Wednesday")
    if w==4:
        print("Thursday")
    if w==5:
        print("Friday")
    if w==6:
        print("Saturday")
    j+=1


