class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        Sum = 0
        h = set()
        maxsum = 0
        left = 0
        for i in range(n):
            while nums[i] in h:
                h.discard(nums[left])
                Sum -= nums[left]
                left += 1
            
            h.add(nums[i])
            Sum += nums[i]
            
            if i - left >= k:
                h.discard(nums[left])
                Sum -= nums[left]
                left +=1
                
            if i - left + 1 == k:
                maxsum = max(maxsum , Sum)
                
        return maxsum
