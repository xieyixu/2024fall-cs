class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
n=int(input())
visited=set()
root=[TreeNode(i+1) for i in range(n)]
for i in range(n):
    x,y=map(int,input().split())
    if x!=-1:
        root[i].left=root[x-1]
        visited.add(x)
    if y!=-1:
        root[i].right=root[y-1]
        visited.add(y)
a=0
for i in range(n):
    if i+1 not in visited:
        a=i+1
        break
tree=root[a-1]
def dfs(root,h=0):
    if not root:
        return h
    return max(dfs(root.left,h+1),dfs(root.right,h+1))
print(dfs(tree,0))