class CustomStack:

    def __init__(self, maxSize: int):
        self.n=maxSize
        self.s=[]

    def push(self, x: int) -> None:
        if len(self.s) < self.n :
            self.s.append(x)

    def pop(self) -> int:
        if self.s :
            x=self.s[-1]
            self.s=self.s[:len(self.s)-1]
            return x
        else :
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.s))) :
            self.s[i]=self.s[i]+val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)