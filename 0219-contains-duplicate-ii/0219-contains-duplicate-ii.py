class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        left = 1
        myhash = {}
        
        for r in range(len(nums)):
            if nums[r] not in myhash:
                myhash[nums[r]] = r
            elif abs(myhash[nums[r]] - r) <= k:
                return True
            else:
                myhash[nums[r]] = r
            
        return False
    
                