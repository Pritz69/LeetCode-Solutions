class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=collections.defaultdict(list)
        for i,eq in enumerate(equations) :
           a,b=eq
           adj[a].append([b,values[i]])
           adj[b].append([a,1/values[i]])
        ans =[]
        def bfs(src,tar) :
            if src not in adj or tar not in adj :
                return -1
            q,visit=deque(),set()
            q.append([src,1])
            visit.add(src)
            while q :
                n,w=q.popleft()
                if n==tar :
                    return w
                for nei,weight in adj[n] :
                    if nei not in visit :
                        q.append([nei,w*weight])
                        visit.add(nei)
            return -1
        for q in queries :
            ans.append(bfs(q[0],q[1]))
        return ans
