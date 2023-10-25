class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        curr_min = inf
        max_diff = -1

        for num in nums:
            max_diff = max(max_diff, num - curr_min)
            curr_min = min(curr_min, num)

        return max_diff or -1