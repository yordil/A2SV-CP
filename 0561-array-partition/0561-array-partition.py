class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
       
        maxn = 0
        minval = 0
        for i in range(0,len(nums) ,2):
            minval = min(nums[i] , nums[i+1])
            maxn +=minval
            
        return maxn
            
            
                
            
            