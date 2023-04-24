class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert stones to negative numbers for max heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # get the two largest stones
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            # smash the two stones together
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)

        # if there is only one stone left, return its positive value
        if max_heap:
            return -max_heap[0]
        else:
            return 0
