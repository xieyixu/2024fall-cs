stack=[]
m=[]
try:
    while True:
        words=input().split()
        if words[0]=='pop':
            if stack:
                stack.pop()
                if m:
                    m.pop()
        elif words[0]=='min':
            if m:
                print(m[-1])
        else:
            h=int(words[1])
            stack.append(h)
            if not m:
                m.append(h)
            else:
                k=m[-1]
                m.append(min(k,h))          #这个辅助栈非常巧妙，避免了查找过程
except EOFError:
    pass