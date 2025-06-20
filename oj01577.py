class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert_into_bst(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root


def preorder_traversal(root):
    if not root:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

s=[]
while True:
    a=input()
    if a=='$':
        root = None
        for x in reversed(s):
            for leaf in x:
                root = insert_into_bst(root, leaf)
        preorder = preorder_traversal(root)
        print(''.join(preorder))
        break
    elif a=='*':
        root=None
        for x in reversed(s):
            for leaf in x:
                root=insert_into_bst(root,leaf)
        preorder=preorder_traversal(root)
        print(''.join(preorder))
        s=[]
    else:
        s.append(a)