n=int(input())
names=[]
for _ in range(n):
    name=input()
    names.append(name)
names.sort()
a=int(n/2)
name_1=names[a-1]
name_2=names[a]
n1=len(name_1)
n2=len(name_2)
i=0
answer=[]
while i<n1 and i<n2:
    if name_1[i]==name_2[i]:
        answer.append(name_1[i])
        i+=1
    else:
        answer.append(chr(ord(name_1[i])+1))
        break
print(''.join(answer))