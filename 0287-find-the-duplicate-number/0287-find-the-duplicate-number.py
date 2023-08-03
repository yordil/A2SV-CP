class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        Hash= {}
        
        for i in range(len(nums)):
            if nums[i] not in Hash:
                Hash[nums[i]] = i
            else:
                return nums[i]
            
#O(N) -> space complexity