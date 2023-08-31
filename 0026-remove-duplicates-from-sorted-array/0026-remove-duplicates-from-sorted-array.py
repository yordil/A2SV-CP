class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      
        if len(nums) < 2:
            return len(nums)
        
        left = 0 
        right = 1
        List = []
        l = len(nums)
        counter=0
        
        while right < len(nums):   
           
            if nums[left] == nums[right]:
                nums.pop(left)
                
               
            else:
                left = right
                right+=1
                
        return len(nums)
                
                
        
       