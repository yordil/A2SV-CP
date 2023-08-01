class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums and nums.count(target) > 1:
            return [nums.index(target) , nums.index(target)+nums.count(target)-1]
        elif target in nums and nums.count(target) == 1:
            return [nums.index(target) , nums.index(target)]
        return [-1 , -1]