class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        counter = 0
        count = 0
        for i in nums:
            if i:
                count +=1
            else:
                counter = max(counter, count)
                count = 0

        return max(counter , count)