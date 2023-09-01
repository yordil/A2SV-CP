class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        myhash = {}
        left = 1
      
        
        for i in range(len(nums)):
            if nums[i] in myhash and abs(myhash.get(nums[i]) - i) <=k:
                return True
            
            myhash[nums[i]] = i
                
        return False