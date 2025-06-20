class Union_find:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
        self.enemy=[-1]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX!=rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.parent[rootY]=rootX
            elif self.rank[rootY]>self.rank[rootX]:
                self.parent[rootX]=rootY
            else:
                self.parent[rootY]=rootX
                self.rank[rootX]+=1
    def set_enemy(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        if self.enemy[rootX]==-1:
            self.enemy[rootX]=rootY
        else:
            self.union(self.enemy[rootX],rootY)
        if self.enemy[rootY]==-1:
            self.enemy[rootY]=rootX
        else:
            self.union(self.enemy[rootY],rootX)
def solve():
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        uf=Union_find(n)
        for _ in  range(m):
            query=input().split()
            if query[0]=='A':
                a,b=int(query[1])-1,int(query[2])-1
                if uf.find(a)==uf.find(b):
                    print('In the same gang.')
                elif uf.enemy[uf.find(a)]==uf.enemy[uf.find(b)]:
                    print('In different gangs.')
                else:
                    print('Not sure yet.')
            else:
                a, b = int(query[1]) - 1, int(query[2]) - 1
                uf.set_enemy(a,b)
if __name__=='__main__':
    solve()