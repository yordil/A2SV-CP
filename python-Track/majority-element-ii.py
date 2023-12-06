class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        more = floor(nums_size/ 3)
   
        return  set(filter(lambda x : nums.count(x) > more , nums))







#         answer = []
#         nums.sort()
        
#         x  = 1 
        
#         for i in range(0 , len(nums) , x):
#             x  = nums.count(nums[i])
#             if x > more:
#                 answer.append(nums[i])
                
#         return nums
         
     