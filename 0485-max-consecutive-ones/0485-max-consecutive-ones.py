class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        flag = 0 
        copy = 0
        
        for i in range(len(nums)):
            
            if nums[i]:
                flag+=1
            else:
                copy = max(copy , flag)
                flag = 0
                
                
        return max(copy , flag)