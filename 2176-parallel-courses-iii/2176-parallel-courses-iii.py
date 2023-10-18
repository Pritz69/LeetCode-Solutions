class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjlist=defaultdict(list)
        for src,dst in relations :
            adjlist[src].append(dst)
        maxcost={}
        def dfs(src) :
            if src in maxcost :
                return maxcost[src]
            res=time[src-1]
            for dst in adjlist[src] :
                res = max(res, time[src-1] + dfs(dst))
            maxcost[src]=res
            return res
        for i in range(1,n+1) :
            dfs(i)
        return max(maxcost.values())