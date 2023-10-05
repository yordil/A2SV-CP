class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        counter = [0] * (max(nums)+1)
        result = [0] * len(nums)
        
        
        for i in range(len(nums)):  
            counter[nums[i]] +=1
            
        for i in range( 1 , len(counter)):
            counter[i] += counter[i-1];
            
        for i in range(len(result)):
            if nums[i] == 0:
                result[i] = 0
            else:
                result[i] = counter[nums[i]-1]
            
        return result
            
            