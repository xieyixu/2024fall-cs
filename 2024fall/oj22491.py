def score(h,s):
    s1=[[s[i][0],s[i][1],s[i][0]*s[i][1]] for i in range(len(s))]
    s1.sort(key=lambda x:x[2],reverse=True)
    total=0
    i=0
    while h>0 and i<len(s1):
        decrease=5/s1[i][0]
        if h>=decrease:
            h-=decrease
            total+=5*s1[i][1]
        else:
            total+=h*s1[i][1]*s1[i][0]
            return total
        i+=1
    return total

h=int(input())
m=int(input())
s=[list(map(float,input().split())) for _ in range(m)]
s1=[s[i][0]*s[i][1] for i in range(m)]
h=2*h-m*0.5
print(round(score(h,s),1))