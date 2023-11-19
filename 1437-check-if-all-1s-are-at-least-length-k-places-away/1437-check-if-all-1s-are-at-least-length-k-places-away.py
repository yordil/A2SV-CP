class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        myhash = {}
        
        for i , v in enumerate(nums):
            if v == 1:
                if 1 in myhash and i - myhash[1] <= k:
                    return False
                myhash[1] = i
                    
        return True
            