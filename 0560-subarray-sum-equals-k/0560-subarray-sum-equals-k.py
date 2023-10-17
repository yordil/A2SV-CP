class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        myhash = {0:1}
        
        psum = 0 
        result = 0
        for i in range(len(nums)):
            psum +=nums[i]
            diff = psum - k
            
            result += myhash.get(diff , 0)
            
            myhash[psum] =1 + myhash.get(psum , 0)
            
        return result
                
        
            
            
            
                
            
            
            
            
            