class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        
        l = 0 
        zeroCount = 0
        ans   = 0
        for r in range(len(nums)):
            if not nums[r]:
                zeroCount +=1

            while zeroCount > k:
                if not nums[l]:
                    zeroCount -=1
                
                l+=1

            ans  = max(ans , r - l + 1)

        return ans 

      


