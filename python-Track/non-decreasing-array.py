class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        

        for i in range(len(nums) - 1):
            if i == 0 and nums[i] > nums[i+1]:
                nums[i] = nums[i+1]
                break
            elif i > 0 and nums[i] > nums[i+1]:
                if nums[i+1] < nums[i-1]:
                    nums[i+1] = max(nums[:i+1])
                else:
                    nums[i] = nums[i+1]
                break
            
        print(nums)
        return sorted(nums) == nums
