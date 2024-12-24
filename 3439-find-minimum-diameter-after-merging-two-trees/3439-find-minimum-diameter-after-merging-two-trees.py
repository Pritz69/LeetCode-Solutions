class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def farthest(G, i):
            n = len(G)
            bfs = [i]
            seen = [0] * n
            seen[i] = 1
            res = maxd = -1
            for i in bfs:
                for j in G[i]:
                    if seen[j] == 0:
                        seen[j] = seen[i] + 1
                        bfs.append(j)
                        if seen[j] > maxd:
                            res = j
                            maxd = seen[j]
            return res, maxd - 1

        def diameter(edges):
            if not edges:
                return 0,0,0
            n = len(edges) + 1
            G = [[] for i in range(n)]
            for i,j in edges:
                G[i].append(j)
                G[j].append(i)
            v1, d = farthest(G, 0)
            v2, d = farthest(G, v1)
            return d,v1,v2

        d1, i, j = diameter(edges1)
        d2, i, j = diameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
        