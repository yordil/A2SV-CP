class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        N = numBottles
        ans = numBottles
        remain = 0
        while N > 0:
            prev =  N // numExchange
            remain += N % numExchange

            if prev == 0:
                if remain + prev >= numExchange:
                    remain -=numExchange
                    N = numExchange
                    continue
                else:
                    break
            else:
                N = prev 

            ans += prev
        return ans