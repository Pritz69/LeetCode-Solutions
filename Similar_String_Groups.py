from collections import defaultdict
class Solution:
    def dfs(self, node, adj, visit):
        visit[node] = True
        if node not in adj:
            return
        for neighbor in adj[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                self.dfs(neighbor, adj, visit)

    def isSimilar(self, a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff == 0 or diff == 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)

        visit = [False] * n
        count = 0
        for i in range(n):
            if not visit[i]:
                self.dfs(i, adj, visit)
                count += 1

        return count
