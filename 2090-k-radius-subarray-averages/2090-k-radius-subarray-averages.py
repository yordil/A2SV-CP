class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        # if len(nums) < 2:
        #     return nums
        
        List=[-1] * len(nums)
                               
        left_pointer = 0 
        right = 2*k
        divisor = 2*k + 1
        Sum = 0 
        
        
        i = k;
        
        while i < len(nums)-k:
            if i == k:
                Sum= sum(nums[left_pointer:right+1])
                average = Sum / divisor
                List[i] = floor(average)
            else:
                # average = Sum / divisor
                right +=1
                Sum += -nums[left_pointer] + nums[right]
                List[i] = floor(Sum/divisor)
                left_pointer +=1  
               
            
            i +=1
        
#         for i in range(k,len(nums)):
#              if  i+k < len(nums):
                
            
            
                
                
        return List