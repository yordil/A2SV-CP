class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        maxavg = -inf
        left = 0
        Sum = 0
        for i in range(n):
            Sum += nums[i]
            
            if i + 1 >= k:
                maxavg = max(maxavg , Sum/k)
                Sum -= nums[left]
                left +=1
                
        return maxavg
                