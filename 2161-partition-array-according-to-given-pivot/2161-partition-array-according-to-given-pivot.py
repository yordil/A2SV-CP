class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less= []
        greater = []
        eq = []
        
        for i in range(len(nums)):
           
            if nums[i] > pivot:
                greater.append(nums[i])
            elif nums[i] < pivot:
                less.append(nums[i])
            else:
                eq.append(nums[i])
                
        return less + eq + greater
                