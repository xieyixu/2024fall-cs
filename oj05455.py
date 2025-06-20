class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def build_tree(root,value):
    if root is None:
        return TreeNode(value)
    if value<root.val:
        root.left=build_tree(root.left,value)
    elif value>root.val:
        root.right=build_tree(root.right,value)
    return root

from collections import deque

nums=list(map(int,input().split()))
tree=None
for num in nums:
    tree=build_tree(tree,num)

queue=deque([tree])
ans=[]
while queue:
    x=queue.popleft()
    if x:
        ans.append(x.val)
    if x.left:
        queue.append(x.left)
    if x.right:
        queue.append(x.right)
print(' '.join(map(str,ans)))