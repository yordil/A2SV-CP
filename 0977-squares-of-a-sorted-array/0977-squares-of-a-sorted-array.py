class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right =len(nums)-1
        List= [0] * len(nums)
        i = len(nums) -1
        
        
        while left <= right :
            if abs(nums[left]) > abs(nums[right]):
                List[i] = (nums[left] **2)          
                left+=1
            else: 
                List[i] = nums[right] ** 2
                right -=1
            i -= 1
        
        return List
                
                
                
            