class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum , l = 0 , 0
        minlen = inf
        for r in range(len(nums)):
            Sum += nums[r]
            while Sum >= target:
                Sum -= nums[l]
                minlen = min(minlen, r - l +1)
                l+=1
        return minlen if minlen != inf else 0               
                
            
   











































          # minval = inf
        
#         L = 0 
#         Sum = 0 
#         for R in range(len(nums)):
#             Sum += nums[R]
            
#             while Sum >= target:
#                 minval = min(minval , R-L + 1)
#                 Sum -=nums[L]
#                 L+=1
               
                
            
                
#         return 0 if minval == inf else minval
                
        
        
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


# we can implment using float flag 
                