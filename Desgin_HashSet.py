class MyHashSet:

    def __init__(self):
        self.l=defaultdict(int)

    def add(self, key: int) -> None:
        self.l[key] = 1

    def remove(self, key: int) -> None:
        self.l[key] = 0

    def contains(self, key: int) -> bool:
        return self.l[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
