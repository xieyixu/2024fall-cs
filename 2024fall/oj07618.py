n=int(input())
a=[]
answer=[]
for i in range(n):
    id,age=input().split()
    Age=int(age)
    a.append([id,Age])
b=[p for p in a if p[1]>=60]
c=[p for p in a if p[1]<60]
b.sort(key=lambda x:-x[1])
for i in range(len(b)):
    answer.append(b[i][0])
for i in range(len(c)):
    answer.append(c[i][0])
for s in answer:
    print(s)