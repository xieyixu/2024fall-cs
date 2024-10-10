import math
t=[]
while True:
    n=int(input())
    if n!=0:
        students=[]
        for i in range(n):
            student=list(map(int,input().split()))
            students.append(student)
        times=[]
        for i in range(n):
            if students[i][1]>=0:
                time=students[i][1]+math.ceil((4.5/(students[i][0]))*3600)
                times.append(time)
        t.append(min(times))
    if n==0:
        break

for time in t:
    print(time)