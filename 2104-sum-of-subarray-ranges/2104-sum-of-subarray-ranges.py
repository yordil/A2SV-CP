class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 2:
            return 0
        Sum = 0
      
        for i in range(len(nums)):
            minv, maxv  = math.inf , -math.inf
            for j in range(i , len(nums)):
                maxv = max(maxv , nums[j])
                minv = min(minv , nums[j])
                Sum += maxv - minv
        return Sum