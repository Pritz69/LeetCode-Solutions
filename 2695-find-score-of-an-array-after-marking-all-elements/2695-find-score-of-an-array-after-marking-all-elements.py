class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        heap = [(nums[i], i) for i in range(n)]  
        heapq.heapify(heap)  
        marked = set()  
        ans = 0

        while heap:
            value, index = heapq.heappop(heap) 
            if index in marked:
                continue  
            ans += value
            marked.add(index)
            if index - 1 >= 0:
                marked.add(index - 1)
            if index + 1 < n:
                marked.add(index + 1)
        
        return ans