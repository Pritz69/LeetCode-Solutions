class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.n = 0

    def consec(self, num: int) -> bool:
        if num == self.v:
            self.n += 1
        else:
            self.n = 0

        return self.n >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
