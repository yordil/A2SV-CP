class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        prefix = 0 
        
        my_dict = {0:0}
        for i in range(n):
            prefix +=nums[i]
            
            if prefix % k not in my_dict:
                my_dict[prefix % k] = i+1
            elif my_dict[prefix%k] < i:
                return True
            
        return False
                
            