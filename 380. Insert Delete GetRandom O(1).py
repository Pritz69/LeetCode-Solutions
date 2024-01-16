class RandomizedSet:

    def __init__(self):
        self.s={}
        self.l=[]
    def insert(self, val: int) -> bool:
        if val in self.s :
            return False
        else :
            self.s[val]=len(self.l)
            self.l.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.s :
            idx=self.s[val]
            lastelmnt=self.l[-1]
            self.l[idx]=lastelmnt
            self.l.pop()
            self.s[lastelmnt]=idx
            del self.s[val]
            return True
        else :
            return False

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
