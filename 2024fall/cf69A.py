n=int(input())
i=0
sx=0
sy=0
sz=0
while i<n:
    x,y,z=map(int,input().split())
    sx=sx+x
    sy=sy+y
    sz=sz+z
    i+=1
if  sx==0 and sy==0 and sz==0:
    print("YES")
else :
    print("NO")