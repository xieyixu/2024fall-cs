s=input()
s=s.lower()
j=1
i=1
for j in range(1,len(s)):
    if s[j]==s[j-1]:
        i=i+1
    else:
        print(f"({s[j-1]},{i})",end="")
        i=1
print(f"({s[len(s)-1]},{i})")