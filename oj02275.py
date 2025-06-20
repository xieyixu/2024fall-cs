class Node:
    def __init__(self,name):
        self.name=name
        self.dirs=[]
        self.files=[]
def print_directory(root,m):
    pre='|     '*m
    print(pre+root.name)
    for Dir in root.dirs:
        print_directory(Dir,m+1)
    for file in sorted(root.files):
        print(pre+file)
tests,test=[],[]
while True:
    s=input()
    if s=='#':
        break
    elif s=='*':
        tests.append(test)
        test=[]
    else:
        test.append(s)
for n,test in enumerate(tests,1):
    root=Node('ROOT')
    stack=[root]
    print(f'DATA SET {n}:')
    for i in test:
        if i[0]=='d':
            Dir=Node(i)
            stack[-1].dirs.append(Dir)
            stack.append(Dir)
        elif i[0]=='f':
            stack[-1].files.append(i)
        else:
            stack.pop()
    print_directory(root,0)
    print()