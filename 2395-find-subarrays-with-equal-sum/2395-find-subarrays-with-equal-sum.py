class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        myHash={}
        
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] in myHash:
                return True
            else:
                myHash[nums[i] + nums[i+1]] = i
        return False