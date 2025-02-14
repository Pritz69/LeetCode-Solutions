class ProductOfNumbers:

    def __init__(self):
        self.lp = [1]  

    def add(self, num: int) -> None:
        if num == 0:
            self.lp = [1]
        else:
            self.lp.append(self.lp[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.lp):
            return 0
        return self.lp[-1] // self.lp[-k - 1]