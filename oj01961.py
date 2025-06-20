def lps(s):
    n=len(s)
    l=[0]*n
    length=0
    i=1
    while i<n:
        if s[i]==s[length]:
            length+=1
            l[i]=length
            i+=1
        else:
            if length!=0:
                length=l[length-1]
            else:
                l[i]=0
                i+=1
    return l
i=0

while True:
    N=int(input())
    if N==0:
        break
    i+=1
    S=input()
    l=lps(S)
    print(f'Test case #{i}')
    for j in range(1,N):
        length=j+1
        prefix_len=length-l[j]
        if length%prefix_len==0:
            K=length//prefix_len
            if K>1:
                print(f'{length} {K}')
    print('')