class Treenode:
    def __init__(self):
        self.left=None
        self.right=None
def build_tree(dfs_string):
    root=Treenode()
    stack=[root]
    for c in dfs_string:
        node=Treenode()
        if c=='d':
            stack[-1].left=node
            stack.append(node)
        if c=='u':
            stack.pop()
            if stack:
                parent=stack[-1]
                if parent.left is not None:
                    temp=parent.left
                    while temp.right is not None:
                        temp=temp.right
                    temp.right=node
    return root
def get_height(root):
    if not root:
        return 0
    height=1
    child=root.left
    while child:
        height=max(height,1+get_height(child))
        child=child.right
    return height
dfs_string=input()
stack_depth=0
max_depth=0
for c in dfs_string:
    if c=='d':
        stack_depth+=1
        max_depth=max(max_depth,stack_depth)
    if c=='u':
        stack_depth-=1
h1=max_depth
root=build_tree(dfs_string)
h2=get_height(root)
print(f'{h1} => {h2}')