class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        
        
        
        for r in range(0 , len(nums)-1):
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0);  
            else:
                left = left + 1
                
            
            
            
                
              
            
                
                
                
        