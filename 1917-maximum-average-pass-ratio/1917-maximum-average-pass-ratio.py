class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b

        maxHeap = []
        for a, b in classes:
            maxHeap.append((-profit(a, b), a, b))
        heapq.heapify(maxHeap) 

        for _ in range(extraStudents):
            d, a, b = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-profit(a + 1, b + 1), a + 1, b + 1))

        return sum(a / b for d, a, b in maxHeap) / len(classes)