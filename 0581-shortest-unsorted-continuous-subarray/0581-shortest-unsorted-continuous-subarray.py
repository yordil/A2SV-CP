class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1   
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1
        if l == len(nums) - 1:
            return 0
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1     
        min_val = min(nums[l:r + 1])
        max_val = max(nums[l:r + 1]) 
        while l >= 0 and nums[l] > min_val:
            l -= 1

        while r < len(nums) and nums[r] < max_val:
            r += 1

        return r - l - 1

#     The time is O(N) and space is O(N) - > two pointer appraoch used by modifying prevision submission :

