n=int(input())
a=bin(n)[2:]
j=0
for i in range(len(a)):
    if a[i]!=a[len(a)-i-1]:
        j=1
        break
if j==1:
    print("No")
else:
    print("Yes")
