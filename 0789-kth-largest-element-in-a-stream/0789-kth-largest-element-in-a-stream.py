class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minh,self.k=nums,k
        heapq.heapify(self.minh)
        while (len(self.minh) > self.k) :
            heapq.heappop(self.minh)

    def add(self, val: int) -> int:
        heapq.heappush(self.minh,val)
        if (len(self.minh) > self.k) :
            heapq.heappop(self.minh)
        return self.minh[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)