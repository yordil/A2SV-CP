class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #  In the constraint the max len is 100 so

        count = 0

        for i in range(len(nums)-1):
            for j in range(i+1 , (len(nums))):
                if i < j and nums[i] == nums[j]:
                    count+=1

        return count