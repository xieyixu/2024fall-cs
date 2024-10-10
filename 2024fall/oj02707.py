import math
n=int(input())
factors=[]

for i in range(n):
    factor=list(map(float,input().split()))
    factors.append(factor)

for i in range(n):
    delta=factors[i][1]**2-4*factors[i][0]*factors[i][2]
    if delta>0:
        x1=(-factors[i][1]+math.sqrt(delta))/(2*factors[i][0])
        x2=(-factors[i][1]-math.sqrt(delta))/(2*factors[i][0])
        print(f"x1={x1:.5f};x2={x2:.5f}")
    elif delta==0:
        x1=(-factors[i][1])/(2*factors[i][0])
        print(f"x1=x2={x1:.5f}")
    else:
        if factors[i][1]==0:
            Re=0
            Im = math.sqrt(-delta) / (2 * factors[i][0])
        else:
            Re=(-factors[i][1])/(2*factors[i][0])
            Im=math.sqrt(-delta)/(2*factors[i][0])
        print(f"x1={Re:.5f}+{Im:.5f}i;x2={Re:.5f}-{Im:.5f}i")