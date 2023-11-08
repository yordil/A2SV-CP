class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix = [0] *1001
        
        for t in trips:
            num , fro , to = t
            prefix[fro] +=num
            prefix[to] -=num
            
        sumofppl = 0
        for i in range(1001):
            sumofppl += prefix[i]
            if sumofppl > capacity:
                return False
            
        return True