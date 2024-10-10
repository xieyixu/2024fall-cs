def function(a):
    if a<60:
        return False
    else:
        i=3
        n=[]
        while i<=360:
            if 360%i==0:
                m=180-360/i
                n.append(m)
            i+=1
        if a in n:
            return True
        else:
            return False


n=int(input())
angles=[int(input())for _ in range(n)]
for angle in angles:
    if function(angle):
        print("YES")
    else:
        print("NO")