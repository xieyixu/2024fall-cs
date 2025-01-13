s=input()
n=len(s)
result=s[0]
max_length=0
i=0;j=1
while i<n and j<n:
    if s[j] not in s[i:j]:
        j+=1
        if j-i>max_length:
            result=s[i:j]
            max_length=j-i
    else:
        i+=1
if n==1:
    max_length=1
print(max_length)