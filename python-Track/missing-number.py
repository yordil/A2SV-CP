class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set2 = set(range(0 , max(nums)+1))
        ans = list(set(nums) ^ set2)
        return ans[0] if ans else max(nums)+1