class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[len(nums)-1]
        b = nums[len(nums)-2]
        return  (a-1) * (b-1)