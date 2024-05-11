class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs=[]
        for i in range(len(wage)) :
            pairs.append((wage[i]/quality[i],quality[i]))
        pairs.sort()
        res=float('inf')
        totq=0
        h=[]
        for rate,q in pairs :
            heapq.heappush(h,-q)
            totq += q
            if len(h) > k :
                ql = -heapq.heappop(h)
                totq -= ql
            if len(h) == k :
                res=min(res,totq*rate)
        return res
