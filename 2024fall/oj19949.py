def string1(s):
    count1=0
    i=0
    while i <=len(s)-3:
        if s[i:i+3]=='###':
            count1+=1
            i=i+3
        else:
            i+=1
    return count1

def string2(s):
    count2=0
    i=0
    while i<=len(s)-6:
        if s[i:i + 6] =='######':
            count2+=1
            i = i + 6
        else:
            i+=1
    return count2

n=int(input())
i=0
sum=0
sentences=[]
while i<n:
    s=input()
    sentences.append(s.replace(" ",""))
    i+=1
for i in range(n):
    a=int(string1(sentences[i]))
    b=int(string2(sentences[i]))
    sum+=a/2-b
print(int(sum))