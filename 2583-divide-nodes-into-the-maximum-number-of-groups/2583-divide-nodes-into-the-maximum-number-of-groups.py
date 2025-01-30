class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        def BFS(node):
            q = deque([(node,1)])
            seen = {node:1}
            level = 1
            while q:
                cur,level = q.popleft()
                for nei in graph[cur]:
                    if nei not in seen:
                        seen[nei] = level+1
                        q.append((nei,level+1))
                    elif seen[nei]==level: 
                        return -1
            return level
        
        ### DFS to find the connected component
        def dfs(node):
            nonlocal visited
            nonlocal connectedComponent
            for nei in graph[node]:
                if nei not in connectedComponent:
                    connectedComponent.add(nei)
                    dfs((nei))
                    visited.add(nei)

        graph = defaultdict(list)
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        maxGroup = []
        visited = set()
        for i in range(1,n+1):
            if i not in visited:
                connectedComponent = {i}
                
                ### Using DFS to find the connect component
                dfs(i)
                
                maxGroup.append(0)
                for i in connectedComponent:
                    groups = BFS(i)
                    if groups==-1:
                        return -1
                    maxGroup[-1] = max(maxGroup[-1],groups)

        return sum(maxGroup)