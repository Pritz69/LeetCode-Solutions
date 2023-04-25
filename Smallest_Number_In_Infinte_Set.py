import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.pq=[]
        self.set=set()
        for i in range(1,1001) :
            heapq.heappush(self.pq,i)
            self.set.add(i)

    def popSmallest(self) -> int:
        x=heapq.heappop(self.pq)
        self.set.remove(x)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.set :
            heapq.heappush(self.pq,num)
            self.set.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
