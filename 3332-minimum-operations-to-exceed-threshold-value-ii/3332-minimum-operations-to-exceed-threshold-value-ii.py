class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
        operations = 0
        while len(heap) > 1 and heap[0] < k:
            x = heappop(heap)
            y = heappop(heap)
            new_element = x*2 + y
            heappush(heap, new_element)
            operations += 1
        return operations