class MyQueue:

    def __init__(self):
        self.st=[]        

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        x=self.st.pop(0)
        return x
    def peek(self) -> int:
        s=self.st[0]
        return s

    def empty(self) -> bool:
        return len(self.st)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
