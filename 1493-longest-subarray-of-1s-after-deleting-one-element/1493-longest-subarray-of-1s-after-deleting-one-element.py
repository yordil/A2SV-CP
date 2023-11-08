from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mywindow = deque()
        zerocount = 0
        maxlen = 0
        
        for i in range(len(nums)):
            mywindow.append(nums[i])
            
            if nums[i] == 0:
                zerocount += 1
            
            while zerocount > 1:
                if mywindow.popleft() == 0:
                    zerocount -= 1
            
            maxlen = max(maxlen, len(mywindow)-1)

        return maxlen

            