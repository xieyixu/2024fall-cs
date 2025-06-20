class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def build_tree(s,index):
    if index[0]>=len(s):
        return None
    char=s[index[0]]
    index[0]+=1
    if char=='.':
        return None
    node=TreeNode(char)
    node.left=build_tree(s,index)
    node.right=build_tree(s,index)
    return node
def inorder(root):
    if not root:
        return []
    if root:
        return inorder(root.left)+[root.val]+inorder(root.right)
def postorder(root):
    if not root:
        return []
    if root:
        return postorder(root.left)+postorder(root.right)+[root.val]
s=input()
index=[0]
root=build_tree(s,index)
ans_1=inorder(root)
ans_2=postorder(root)
print(''.join(ans_1))
print(''.join(ans_2))