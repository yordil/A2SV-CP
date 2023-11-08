class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxval = 0
        for r , num in enumerate(nums):
            k -=1 - num
            
            if k < 0:
                k += 1 - nums[left]
                left +=1
            else:
                maxval = max(maxval , r-left+1)
             
        return maxval
    
    
    
    
    
    
    
    
    
    
    # left = 0
        # ans = 0
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count += 1
        #     while count > k:
        #         if nums[left] == 0:
        #             count -= 1
        #         left += 1
        #     ans = max(ans, i - left + 1)
        # return ans