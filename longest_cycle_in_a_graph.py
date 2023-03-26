class Solution(object):
    answer = -1
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        dist = dict()
        n = len(edges)
        visit = [0]*n

        for node in range(n):
            if not visit[node]:
                dist = {}
                dist[node] = 1
                self.dfs(node, edges, dist, visit)
        return self.answer
    
    def dfs(self, node, edges, dist, visit):
        visit[node] = 1
        nei = edges[node]
        if nei != -1 and not visit[nei]:
            dist[nei] = dist[node] + 1
            self.dfs(nei, edges, dist, visit)
        else:
            if nei in dist:
                self.answer = max(self.answer, dist[node] - dist[nei] + 1)
