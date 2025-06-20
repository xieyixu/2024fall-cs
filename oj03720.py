class Node:
    def __init__(self,x,depth):
        self.x=x
        self.depth=depth
        self.left=None
        self.right=None

    def preorder(self):
        nodes=[self.x]
        if self.left and self.left.x!='*':
            nodes+=self.left.preorder()
        if self.right and self.right.x!='*':
            nodes+=self.right.preorder()
        return nodes

    def inorder(self):
        nodes=[]
        if self.left and self.left.x!='*':
            nodes+=self.left.inorder()
        nodes.append(self.x)
        if self.right and self.right.x!='*':
            nodes+=self.right.inorder()
        return nodes

    def postorder(self):
        nodes=[]
        if self.left and self.left.x!='*':
            nodes+=self.left.postorder()
        if self.right and self.right.x!='*':
            nodes+=self.right.postorder()
        nodes.append(self.x)
        return nodes

def build_tree():
    n=int(input())
    for _ in range(n):
        tree=[]
        stack=[]
        while True:
            s=input()
            if s=='0':
                break
            depth=len(s)-1
            node=Node(s[-1],depth)
            tree.append(node)

            while stack  and tree[stack[-1]].depth>=depth:
                stack.pop()
            if stack:
                parent=tree[stack[-1]]
                if not parent.left:
                    parent.left=node
                else:
                    parent.right=node
            stack.append(len(tree)-1)
        yield tree[0]

for root in build_tree():
    print(''.join(root.preorder()))
    print(''.join(root.postorder()))
    print(''.join(root.inorder()))
    print()