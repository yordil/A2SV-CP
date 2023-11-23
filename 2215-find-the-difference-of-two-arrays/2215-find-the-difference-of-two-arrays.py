class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        myhash = defaultdict(set)
        
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                myhash[0].add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                myhash[1].add(nums2[i])
                
        return list([myhash[0] , myhash[1]])
        
            
            