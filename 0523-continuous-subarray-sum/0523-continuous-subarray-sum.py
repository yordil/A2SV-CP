class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <2:
            return False
        
        
        prefix = 0 
        
        my_dict = {0:-1}
        
        for i in range(n):
            prefix +=nums[i]
            
            prefix %=k
            if prefix in my_dict:
                if i - my_dict[prefix]  > 1: 
                    return True
            else:
                my_dict[prefix] = i
            
            
        return False
                
#             using map by initial value {0:0} and store [prefixsum % k] = i+1 else if dict[prefix % k] < i return True