class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = [-1] * len(nums1)
        
        myhash = {value : index for index , value in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            if nums2[i] not in myhash:
                continue
                
            for j in range(i+1 , len(nums2)):
                if nums2[j] > nums2[i]:
                    indexx = myhash[nums2[i]]
                    ans[indexx] = nums2[j]
                    break
                    
        return ans
                
            
            
        
            
        