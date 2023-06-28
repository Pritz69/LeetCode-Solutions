class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj=collections.defaultdict(list)
        for i in range(len(edges)) :
            src,dst=edges[i]
            adj[src].append([dst,succProb[i]])
            adj[dst].append([src,succProb[i]])
        h=[(-1,start)]
        q=set()
        while h :
            prob,curr = heapq.heappop(h)
            q.add(curr)
            if curr==end :
                return prob*(-1)
            for nei,edgeprob in adj[curr] :
                if nei not in q :
                    heapq.heappush(h,(prob*edgeprob,nei))
        return 0
