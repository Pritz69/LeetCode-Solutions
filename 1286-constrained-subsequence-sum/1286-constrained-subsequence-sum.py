class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res=nums[0]
        heap=[(-nums[0],0)]
        for i in range(1,len(nums)) :
            while i-heap[0][1] > k :
                heapq.heappop(heap)
            curr = max(nums[i],nums[i]-heap[0][0])
            res = max(res,curr)
            heapq.heappush(heap,(-curr,i))
        return res