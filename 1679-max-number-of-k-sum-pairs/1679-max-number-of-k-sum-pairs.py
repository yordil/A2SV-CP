class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        op = 0 
        
        nums.sort()
        
        left = 0
        right  = len(nums) -1 
        
        while left < right: 
            
            if nums[left] + nums[right] > k:
                right -=1
            elif nums[left] + nums[right] < k:
                left +=1
            else:
                op +=1
                left+=1
                right-=1
                
        return op
            
       # O(N) + O(N) -> O(2*N) // O(N)