
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        maxval = 0
        counter = 0
        myset = set(nums)
        seen = set()
        
        for i in myset:
            temp = i
            counter = 0
            if temp not in seen: 
                while temp in myset:
                    counter +=1
                    seen.add(temp)
                    temp -=1
                
                temp = i+1
                while temp in myset:
                    counter +=1
                 
                    seen.add(temp)
                    
                    temp +=1
                    
                maxval = max(maxval , counter)
                
        return maxval
        
        
        
        
#         myhash = {}
#         
#         for num in nums:  
#             if num not in myhash:
#                 myhash[num] = 1
        
#         n = min(nums)
#         m = max(nums)
# #         updating m var 
#         x = 1
#         for i in range(n , m , x):
            
#             if i in myhash:
#                 x = 1
#                 counter +=1
#                 continue
#             else: 
#                 maxval = max(maxval , counter)
#                 counter = 0
                
#             if maxval > ceil(len(nums)/2) and i+1 not in myhash: 
#                 return maxval
           
#         return  max(maxval , counter)