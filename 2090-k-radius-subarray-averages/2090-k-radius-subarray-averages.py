class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        List = [-1] * len(nums)
        windowsum = 0
        size = 2 * k + 1
        
        for i in range(len(nums)):
            windowsum += nums[i]
            
            if i - size >=0:
                windowsum -=nums[i-size]
            
            
            if i - size >= -1 :
                List[i-k] = floor(windowsum/size)
                
        return List
            