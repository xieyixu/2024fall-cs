def function(a,b,c,d):
    if a+b+c+d==24 or a+b+c-d==24 or a+b-c+d==24 or a+b-c-d==24 or a-b+c+d==24 or a-b+c-d==24 or a-b-c+d==24 or a-b-c-d==24 or -a+b+c+d==24 or -a+b+c-d==24 or -a+b-c+d==24 or -a+b-c-d==24 or -a-b+c+d==24 or -a-b+c-d==24 or -a-b-c+d==24 or -a-b-c-d==24:
        return("YES")
    else:
        return("NO")
m=int(input())
results=[]
i=0
while i<m:
    numbers=input().split()
    a,b,c,d=map(int,numbers)
    result=function(a,b,c,d)
    results.append(result)
    i+=1
for result in results:
    print(result)