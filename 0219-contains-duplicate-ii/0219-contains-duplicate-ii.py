class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        myhash = {}

        for idx , val in enumerate(nums):

            if val in myhash and abs(myhash[val]  - idx) <= k:
                return True
            myhash[val] = idx
        return False
                