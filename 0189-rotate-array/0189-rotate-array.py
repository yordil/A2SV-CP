from collections import deque 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # place holder and seeker approach to solve this problem:
        
        d  = deque(nums)
        
        d.rotate(k)
        
        nums[:] = list(d)
             
            
        
        