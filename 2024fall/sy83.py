def common_prefix(str):
    prefix=str[0]
    for s in str[1:]:
        while not s.startswith(prefix):      #startswith是一个特别有效的工具，可以应用于字符串匹配。
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix

n=int(input())
t=[]
for i in range(n):
    a=input()
    t.append(a)
print(common_prefix(t))