class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
    
        duplicates = []
    
        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                duplicates.append(idx + 1)
            else:
                nums[idx] = -nums[idx]

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicates

            
        