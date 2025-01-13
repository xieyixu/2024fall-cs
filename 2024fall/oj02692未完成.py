import re
coins=['A','B','C','D','E','F','G','H','I','J','K','L']
n=int(input())
for _ in range(n):
    condition1=input()
    condition2=input()
    condition3=input()
    c11,c12=re.findall(r'[A-Z]',condition1);c13=re.findall(r'[a-z]',condition1)
    c21,c22=re.findall(r'[A-Z]',condition2);c23=re.findall(r'[a-z]',condition2)
    c31,c32=re.findall(r'[A-Z]',condition3);c33=re.findall(r'[a-z]',condition3)
    