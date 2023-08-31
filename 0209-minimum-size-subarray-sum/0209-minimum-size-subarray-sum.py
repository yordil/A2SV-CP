class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        if sum(nums) < target:
            return 0
        
        minval = len(nums)
        
        L = 0 
        Sum = 0 
        for R in range(len(nums)):
            Sum += nums[R]
            
            while Sum >= target:
                minval = min(minval , R-L + 1)
                Sum -=nums[L]
                L+=1
               
                
            
                
        return minval
                
        
        
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
#         minval = len(nums)
        
#         L = 0 
#         Sum = 0 
#         for R in range(len(nums)):
             
#             if Sum >= target:
#                 minval = min(minval , R-L + 1)
#                 Sum -=nums[L]
#                 L+=1
               
                
#             Sum += nums[R]
          
    
    # first implmentation
#         return minval
                