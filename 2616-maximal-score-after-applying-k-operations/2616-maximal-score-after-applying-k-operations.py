class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        l=[(-1*x) for x in nums]
        heapq.heapify(l)
        ans=0
        for i in range(k) :
            e=heapq.heappop(l)
            ans += (-1*e)
            heapq.heappush(l,floor(e/3))
        return ans