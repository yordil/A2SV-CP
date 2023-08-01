class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
        
        low , high = 0 , len(nums)-1
        
        while low <= high:
            mid = (low+high) // 2
            
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid -1
            else:
                return mid
        
        return low
                