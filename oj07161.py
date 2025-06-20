class TreeNode:
    def __init__(self,val,children):
        self.val=val
        self.children=[]
def post_order(tree,ans):
    if not tree:
        return
    for y in tree.children:
        post_order(y,ans)
    ans.append(tree.val)
from collections import deque
n=int(input())
answer=[]
for _ in range(n):
    l=list(input().split())
    node_queue=deque()
    for i in range(0,len(l),2):
        node_queue.append((l[i],int(l[i+1])))
    if not node_queue:
        continue
    root_char,root_degree=node_queue.popleft()
    root=TreeNode(root_char,[])
    process_queue=deque()
    process_queue.append((root,root_degree))
    while node_queue and process_queue:
        current_node,degree=process_queue.popleft()
        for _ in range(degree):
            if not node_queue:
                break
            child_char,child_degree=node_queue.popleft()
            child_node=TreeNode(child_char,[])
            current_node.children.append(child_node)
            process_queue.append((child_node,child_degree))

    ans=[]
    post_order(root,ans)
    answer+=ans
print(' '.join(answer))