class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #using kaden's Algorithm can be implmented in O(n) time complexity
        
        cur = 0 
        
        maxval = nums[0]
        
        for n in nums:
            cur = max(cur , 0)
            
            cur += n
            
            maxval = max(maxval , cur)
            
        return maxval
    
    
#using sliding window also we can get the index too

#         curr = 0 
#         maxsum = nums[0]
        
#         maxl , maxr  ,  L = 0 , 0  , 0 
        
#         for r in range(len(nums)):
            
#             if cur < 0:
#                 cur= 0
#                 l = r
                
#             cur += num[r]
            
#             if cur > maxsum:
#                 masxum=cur
                
#                 maxl , maxr = l , r
                
#             return [maxl , maxr]
                
                
            
        

        
      