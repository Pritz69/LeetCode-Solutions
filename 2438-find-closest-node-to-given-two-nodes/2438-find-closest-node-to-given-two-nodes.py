class Solution:
    def dfs(self, node, edges, distance, visited):
        visited[node] = True
        neighbor = edges[node]
        if neighbor != -1 and visited[neighbor] == False:
            distance[neighbor] = distance[node] + 1
            self.dfs(neighbor, edges, distance, visited)

    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)
        ans = -1
        minDist = float("inf")
        dist1 = [0] * n
        dist2 = [0] * n
        visited1 = [False] * n
        visited2 = [False] * n
        self.dfs(node1, edges, dist1, visited1)
        self.dfs(node2, edges, dist2, visited2)

        for currNode in range(n):
            if visited1[currNode] and visited2[currNode] and minDist > max(dist1[currNode], dist2[currNode]):
                minDist = max(dist1[currNode], dist2[currNode])
                ans = currNode

        return ans