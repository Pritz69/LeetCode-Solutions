class MyHashMap:

    def __init__(self):
        self.hashmap=dict()

    def put(self, key: int, value: int) -> None:
        self.hashmap[key]=value

    def get(self, key: int) -> int:
        if key in self.hashmap.keys():
            return self.hashmap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hashmap.keys():
            self.hashmap.pop(key)
