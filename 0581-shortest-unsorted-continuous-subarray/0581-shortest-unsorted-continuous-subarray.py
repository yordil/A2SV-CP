class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # Find the left boundary of the unsorted subarray
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1

        # If the array is already sorted, return 0
        if l == len(nums) - 1:
            return 0

        # Find the right boundary of the unsorted subarray
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        # Find the minimum and maximum values in the unsorted subarray
        min_val = min(nums[l:r + 1])
        max_val = max(nums[l:r + 1])

        # Expand the left boundary to include elements smaller than the minimum
        while l >= 0 and nums[l] > min_val:
            l -= 1

        # Expand the right boundary to include elements larger than the maximum
        while r < len(nums) and nums[r] < max_val:
            r += 1

        # The length of the shortest subarray that, when sorted, makes the whole array sorted
        return r - l - 1
