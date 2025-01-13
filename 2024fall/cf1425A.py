import sys
def max_coinsA(n):
    result=0
    if n==0:
        result=0
    elif n==1:
        result=1
    elif 1<n<=8:
        i=1
        while n>0:
            if n%2==0:
                n=n//2
                if i%2==1:
                    result+=n
            elif n%2!=0:
                n=n-1
                if i%2==1:
                    result+=1
            i+=1
    else:
        i=1
        while n>8:
            if n%2==0 and n%4!=0:
                n=n//2
                if i%2==1:
                    result+=n
            else:
                n=n-1
                if i%2==1:
                    result+=1
            i+=1
        while n>0:
            if n%2==0:
                n=n//2
                if i%2==1:
                    result+=n
            elif n%2!=0:
                n=n-1
                if i%2==1:
                    result+=1
            i+=1
    return result

input=sys.stdin.read()
lines=input.split()
results=[]
T=int(lines[0])
for i in range(1,T+1):
    print(max_coinsA(int(lines[i])))  #这个题关于递归的方法我想了很久，但是对于算法的优化并没有思路。建议使用迭代，并且迭代速度快，就不用备忘录了。