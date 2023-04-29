class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = list(range(n))
        def find(x) :
            if parents[x] != x :
                parents[x]=find(parents[x])
            return parents[x]
        def union(x,y) :
            r1=find(x)
            r2=find(y)
            if r1 != r2 :
                parents[r2]=r1
        edgeList.sort(key=lambda x :x[2])
        q = [(l,u,v,i) for i ,(u,v,l) in enumerate(queries)]
        q.sort()
        m=len(queries)
        ans=[False]*m
        edgsize=len(edgeList)
        edgidx=0
        for qlimit,u,v,i in q :
            while edgidx<edgsize and edgeList[edgidx][2] < qlimit :
                union(edgeList[edgidx][0],edgeList[edgidx][1])
                edgidx +=1
            ans[i] = (find(u)==find(v))
        return ans
