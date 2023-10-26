class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return len(nums)
        
        left = 2
        
        
        for r in range(2 , len(nums)):
            
            if nums[r] != nums[left-2]:
                nums[left] = nums[r]
                left+=1
                
        return left