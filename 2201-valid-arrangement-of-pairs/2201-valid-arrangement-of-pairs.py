class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int) # net out degree 
        for x, y in pairs: 
            graph[x].append(y)
            degree[x] += 1
            degree[y] -= 1
                
        for k in degree: 
            if degree[k] == 1: 
                x = k
                break 
                
        ans = []

        def fn(x): 
            """Return Eulerian path via dfs."""
            while graph[x]: fn(graph[x].pop()) 
            ans.append(x)
        
        fn(x)
        ans.reverse()
        return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]
        