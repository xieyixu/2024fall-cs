def can_say_hello(s):
    target="hello"
    j=0
    for  char in s:
        if char==target[j]:
            j+=1
        if j==len(target):
            return "YES"
    return "NO"

x=input().strip()
print(can_say_hello(x))