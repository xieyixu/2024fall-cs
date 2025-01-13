def len_s(k):
    l=0
    a=len(str(k))
    i=1
    while i<a:
        l+=i*9*(10**(i-1))
        i+=1
    l+=a*(k-10**(a-1)+1)
    return l

def array(k):
    sk=[i for i in range(1,k+1)]
    result=''.join(str(x) for x in sk)
    return result

T=[]
t=int(input())
for _ in range(t):
    n=int(input())
    l=0
    i=1
    while l<n:
        l+=len_s(i)
        i+=1
    arr=array(i-1)
    T.append(arr[len(arr)-(l-n)-1])
for _ in T:
    print(_)