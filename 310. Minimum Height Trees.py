class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1 :
            return [0]
        d=defaultdict(list)
        for u,v in edges :
            d[u].append(v)
            d[v].append(u)
        leaves=deque()
        edgecnt={}
        for src,nei in d.items() :
            if len(nei)==1 :
                leaves.append(src)
            edgecnt[src]=len(nei)
        while leaves :
            if n<=2 :
                return list(leaves)
            for i in range(len(leaves)) :
                node=leaves.popleft()
                n -=1
                for nei in d[node] :
                    edgecnt[nei] -=1
                    if edgecnt[nei]==1 :
                        leaves.append(nei)
