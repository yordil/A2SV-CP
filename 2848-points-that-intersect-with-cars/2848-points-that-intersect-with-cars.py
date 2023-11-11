class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        hashtable = set()
        prefixsum = []
        
        for i in range(len(nums)):
            for j in range(2):
                for k in range(nums[i][0] , nums[i][1]+1):
                    hashtable.add(k)
                
        return len(hashtable)
    