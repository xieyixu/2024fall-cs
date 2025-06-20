import bisect

class FenwickTree:
    def __init__(self,size):
        self.n=size
        self.tree=[0]*(self.n+2)
    def update(self,idx,delta):
        while idx<=self.n:
            self.tree[idx]+=delta
            idx+=idx&-idx
    def query(self,idx):
        res=0
        while idx>0:
            res+=self.tree[idx]
            idx-=idx&-idx
        return res
def main():
    while True:
        n=int(input())
        if n==0:
            break
        a=[]
        for _ in range(n):
            a.append(int(input()))
        sorted_a=sorted(a)
        rank=[bisect.bisect_left(sorted_a,x)+1 for x in a]
        ft=FenwickTree(n)
        ans =0
        for x in reversed(rank):
            ans+=ft.query(x-1)
            ft.update(x,1)
        print(ans)
if __name__=='__main__':
    main()