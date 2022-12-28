class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h=[]
        for x in piles :
            heapq.heappush(h,-x)
        for i in range(k) :
            x = -heapq.heappop(h)
            x -= x//2 
            heapq.heappush(h,-x)
        return (-sum(h)) 
