class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if nums.count(1) == len(nums):
            return len(nums) -1
        mywindow = deque()
        zerocount = 0
        maxlen = 0
        for i in range(len(nums)):
            mywindow.append(nums[i])
            while mywindow.count(0) > 1:
                mywindow.popleft()
                
            maxlen = max(maxlen , len(mywindow)-1)
            
            
        
        return maxlen
            