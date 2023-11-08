class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
       
        #implace sort
        
        left = 0
        right = len(nums) -1
        
        while right > 0 and left < len(nums):
            
            if nums[right] %2 :
                right -=2
            elif nums[left] % 2 == 0:
                left+=2
            else:
                nums[right] , nums[left] = nums[left] , nums[right]
                right -=2
                left +=2
                
        return nums
    
    
    
    
    
    
    
    
    
    
    
    
#         arr =[0] * len(nums)
        
#         even = 0
#         odd = 1
#         for i in range(len(nums)):
#             if nums[i] % 2:
#                 nums[odd] = nums[i]
#                 odd +=2
#             else:
#                 nums[even] = nums[i]
#                 even +=2
#         return nums
                