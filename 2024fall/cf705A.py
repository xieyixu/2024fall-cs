a=int(input())
print("I hate",end="")
i=0
while i<a-1:
    if i%2==0:
        print(" that I love",end="")
    if i%2!=0:
        print(" that I hate",end="")
    i+=1
print(" it")