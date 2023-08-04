class MyHashMap:

    def __init__(self):
        self.Hash = {}

    def put(self, key: int, value: int) -> None:
        self.Hash[key] = value

    def get(self, key: int) -> int:
        if key in self.Hash:
            return self.Hash.get(key)
        return -1
        
    def remove(self, key: int) -> None:
        if key in self.Hash:
            self.Hash.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)