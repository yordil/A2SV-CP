class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        fs = set(nums)
        count = 0 
        l = len(nums)
        s = set()

        for i in range(l):
            j = i 
            while(j<l):
                s.add(nums[j])
                if len(s) == len(fs):
                    count += 1
                j += 1
            s = set()
        
        return count
        