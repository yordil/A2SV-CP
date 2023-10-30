class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        hi = len(nums) - 1
        mid = 0
        # Iterate till all the elements
        # are sorted
        
        while mid <= hi:
            # If the element is 0
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo = lo + 1
                mid = mid + 1
            # If the element is 1
            elif nums[mid] == 1:
                mid = mid + 1
            # If the element is 2
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi = hi - 1