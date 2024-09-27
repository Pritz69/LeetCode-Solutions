class MyCalendarTwo:

    def __init__(self):
        self.nonover=[]
        self.over=[]

    def book(self, start: int, end: int) -> bool:
        for s,e in self.over :
            if end > s and e > start :
                return False
        for s,e in self.nonover :
            if end > s and e > start :
                self.over.append((max(s,start),min(end,e)))
        self.nonover.append((start,end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)