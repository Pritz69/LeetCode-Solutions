class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = list(map(lambda x: -x, gifts))
        heapq.heapify(gifts)
        
        for _ in range(k):
            heapq.heappush(gifts, -int(math.sqrt(-heapq.heappop(gifts))))
        return -sum(gifts)
