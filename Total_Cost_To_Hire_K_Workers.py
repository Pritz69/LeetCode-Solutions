class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l=0
        r=len(costs)-1
        h=[]
        heapq.heapify(h)
        ans=0
        while l<candidates :
            heapq.heappush(h,(costs[l],l))
            l +=1
        while r>=len(costs)-candidates and l<=r :
            heapq.heappush(h,(costs[r],r))
            r -=1
        while k != 0 :
            ans += h[0][0]
            idx = h[0][1]
            heapq.heappop(h)
            if idx < l and l<=r :
                heapq.heappush(h,(costs[l],l))
                l +=1
            elif idx > r and l <= r :
                heapq.heappush(h,(costs[r],r))
                r -=1
            k -=1
        return ans
