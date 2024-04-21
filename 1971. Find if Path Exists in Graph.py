class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d=defaultdict(list)
        for x in edges :
            u,v=x[0],x[1]
            d[u].append(v)
            d[v].append(u)
        s=set()
        def dfs(node) :
            if node == destination:
                return True
            s.add(node)
            for x in d[node]:
                if x not in s:
                    if dfs(x):
                        return True
            return False
        return dfs(source)
            
