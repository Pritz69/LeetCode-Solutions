class MyCalendar:

    def __init__(self):
        self.bookings = []
        self.max_end = 0  

    def book(self, start: int, end: int) -> bool:
        if start >= self.max_end:
            self.bookings.append((start, end))
            self.max_end = max(self.max_end, end)
            return True
        
        for s, e in self.bookings:
            if max(s, start) < min(e, end):  
                return False
        
        self.bookings.append((start, end))
        self.max_end = max(self.max_end, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)