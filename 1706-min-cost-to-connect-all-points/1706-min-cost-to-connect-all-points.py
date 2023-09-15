class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        adj={i:[] for i in range(N)}
        for i in range(N) :
            x1,y1=points[i]
            for j in range(i+1,N) :
                x2,y2=points[j]
                dist=abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        visit=set()
        minh=[[0,0]]
        res=0
        while len(visit) < N :
            cost,point=heapq.heappop(minh)
            if point in visit :
                continue
            res +=cost
            visit.add(point)
            for neiCost,nei in adj[point] :
                if nei not in visit :
                    heapq.heappush(minh,[neiCost,nei])
        return res