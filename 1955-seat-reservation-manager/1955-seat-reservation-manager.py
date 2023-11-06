class SeatManager:
    
    def __init__(self, n: int):
        self.h=[]
        self.h=[i for i in range(1,n+1)]
        heapq.heapify(self.h)

    def reserve(self) -> int:
        v=heapq.heappop(self.h)
        #heapq.heapify(self.h)
        return v
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h,seatNumber)
        #heapq.heapify(self.h)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)