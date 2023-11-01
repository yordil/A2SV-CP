from collections import deque
class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prefix = []

    def add(self, num: int) -> None:
        self.arr.append(num)
        if num == 0:
            self.prefix = []
        else:
            if not self.prefix:
                self.prefix.append(num)
            else:
                self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix):
            return 0
        if k == len(self.prefix):
            return self.prefix[-1]
        return self.prefix[-1] // self.prefix[-k-1]

        
# we can keep product of last K element in the array and we can retrive it in O(1) time

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)