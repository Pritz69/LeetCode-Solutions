class UF :
    def __init__(self,n) :
        self.n=n
        self.parents = list(range(n+1))
    def find(self,x) :
        if self.parents[x] != x :
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    def union(self,x,y) :
        r1=self.find(x)
        r2=self.find(y)
        if r1==r2 :
            return 0
        else :
            self.parents[r2]=r1
        self.n -=1
        return 1
    def isconnected(self) :
        return self.n == 1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice,bob = UF(n) , UF(n)
        cnt = 0
        for t,s,d in edges :
            if t==3 :
                cnt += ( alice.union(s,d) | bob.union(s,d) )
        for t,s,d in edges :
            if t==1 :
                cnt += alice.union(s,d) 
            elif t==2 :
                cnt += bob.union(s,d)
        if bob.isconnected() and alice.isconnected() :
            return len(edges)-cnt
        return -1
