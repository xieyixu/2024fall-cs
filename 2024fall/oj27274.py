s=input()
n=len(s)
m=0
while 2**m<=n:
    m+=1
m-=1
k=[]
for i in range(m+1):
    k+=s[2**i-1]
k_2=[]
if m%2==1:
    for i in range(int((m+1)/2)):
        k_2+=k[i]
        k_2+=k[m-i]
elif m%2==0:
    for i in range(int(m/2)):
        k_2+=k[i]
        k_2+=k[m-i]
    k_2+=k[int(m/2)]
print(''.join(k_2))