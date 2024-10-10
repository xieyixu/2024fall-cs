def function(s):
    p=1
    P=[]
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            p+=1
        elif s[i]==s[i+1]:
            P.append(p)
            p=1
    P.append(p)
    return max(P)

s=input()
print(function(s))