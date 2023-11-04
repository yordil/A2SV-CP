class Solution:
    def minimumDifference(self, nums: List[int], k: int):
        nums.sort()
        min_diff = float('inf')
        n = len(nums)

        if n < k:
            return 0

        for i in range(n - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff
