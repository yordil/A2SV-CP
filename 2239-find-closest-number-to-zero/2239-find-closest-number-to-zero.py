class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        val = float('inf') 
       
        for i in nums:
            val = min(val , abs(i - 0))
            
        return val if val in nums else -val
            