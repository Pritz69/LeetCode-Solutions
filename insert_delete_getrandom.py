class RandomizedSet:

    def __init__(self):
        self.nMap={}
        self.nList=[]

    def insert(self, val: int) -> bool:
        res=val not in self.nMap
        if res:
            self.nMap[val]=len(self.nList)
            self.nList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res=val in self.nMap
        if res:
            idx=self.nMap[val]
            lstele=self.nList[-1]
            self.nList[idx]=lstele
            self.nList.pop()
            self.nMap[lstele]=idx
            del self.nMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.nList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
