class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
       my={}
    
       for i in range(len(nums)):
        comp = target - nums[i]
        if comp in my:
            return [i , my[comp]]
        else:
            my[nums[i]] = i
            