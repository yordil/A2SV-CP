class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        myhash = {}
        
        for i in range(len(nums)):
            myhash[nums[i]] = i
        
        for op in operations:
            replace , newval = op
            temp = myhash[replace]
            
            del myhash[replace]
            myhash[newval] = temp
            
        def customComparator(item):
            return myhash[item]
        
        ans  = list( myhash.keys())
        ans.sort(key=customComparator)
        
        return ans