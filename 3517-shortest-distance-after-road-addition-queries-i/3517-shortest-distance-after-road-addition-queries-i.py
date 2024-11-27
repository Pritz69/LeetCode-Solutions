class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj=[[i+1] for i in range(n)] 
        res=[]
        def func() :
            q=deque()
            v=set()
            q.append((0,0))
            v.add(0)
            while q :
                c,l=q.popleft()
                if c==n-1 :
                    return l
                for x in adj[c] :
                    if x not in v :
                        q.append((x,l+1))
                        v.add(x)
        for s,d in queries :
            adj[s].append(d)
            res.append(func())
        return res