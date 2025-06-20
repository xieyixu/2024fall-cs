class MinHeap:
    def __init__(self):
        self.heap=[]
    def push(self,val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
    def pop_min(self):
        if not self.heap:
            return None
        min_val=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_val
    def _heapify_up(self,index):
        while index>0:
            parent=(index-1)//2
            if self.heap[index]<self.heap[parent]:
                self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
                index=parent
            else:
                break
    def _heapify_down(self,index):
        n=len(self.heap)
        while True:
            left=2*index+1
            right=2*index+2
            smallest=index
            if left<n and self.heap[left]<self.heap[smallest]:
                smallest=left
            if right<n and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest!=index:
                self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
                index=smallest
            else:
                break

n=int(input())
heap=MinHeap()
for _ in range(n):
    nums=list(map(int,input().split()))
    if nums[0]==1:
        heap.push(nums[1])
    else:
        x=heap.pop_min()
        print(x)