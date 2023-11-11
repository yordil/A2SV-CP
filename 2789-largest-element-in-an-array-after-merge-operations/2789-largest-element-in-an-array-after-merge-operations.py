class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        post = [0]
        for i in range(len(nums)-1, 0 , -1):
            if nums[i-1] <= nums[i]:
                nums[i-1] = nums[i] + nums[i-1]
                
        return nums[0]
            