class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        num_size = len(nums)
        
        smaller_list = list(filter(lambda x : x < pivot , nums))
        equal = list(filter(lambda x : x == pivot , nums))
        larger_list = list(filter(lambda x : x > pivot , nums))
        
        return smaller_list + equal + larger_list
        
        