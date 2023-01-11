class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        l={i:[] for i in range(n)}
        for par,child in edges :
            l[par].append(child)
            l[child].append(par)
        
        def dfs(cur,par) :
            t=0
            for child in l[cur] :
                if child==par :
                    continue
                childtime = dfs (child,cur)
                if childtime or hasApple[child]:
                    t += 2 + childtime
            return t
        return dfs(0,-1)
