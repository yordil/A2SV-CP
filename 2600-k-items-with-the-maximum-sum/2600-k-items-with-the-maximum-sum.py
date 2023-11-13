class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        counter = 0
        
        while k > 0:
            if numOnes > 0:
                counter +=1
                numOnes-=1
                
            elif numOnes == 0 and numZeros >0:
                numZeros -=1
                
            else:
                counter -=1
                numNegOnes -=1
                
            k-=1
        return counter