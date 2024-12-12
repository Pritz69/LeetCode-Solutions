class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)) :
            gifts[i]=-gifts[i]
        heapq.heapify(gifts)
        while k :
            n=-1* (heapq.heappop(gifts))
            n=int(n**0.5)
            heapq.heappush(gifts,-n)
            k -=1
        return -1*sum(gifts)
