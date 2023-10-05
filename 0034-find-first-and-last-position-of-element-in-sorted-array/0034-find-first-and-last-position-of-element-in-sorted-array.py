class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftindex = self.binaryhelper(nums , target , False)
        rightindex = self.binaryhelper(nums , target ,True)
        return [leftindex , rightindex]
        
        
    def binaryhelper(self, nums , target , forright):
        left , right  = 0  , len(nums) -1 
        i = -1;
        while left <= right:

            mid=  left + (right - left) //2

            if target > nums[mid]:
                left = mid+1

            elif target < nums[mid]:
                right = mid -1
                 

            else:
                i = mid
                if forright:
                    left = mid +1
                else:
                    right = mid - 1
        return i
        
        
        
        
        
        
        
        
                        

            
        
    
    
    
    
    
    
    
    
#         MY previous implmentation 
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if target in nums and nums.count(target) > 1:
#             return [nums.index(target) , nums.index(target)+nums.count(target)-1]
#         elif target in nums and nums.count(target) == 1:
#             return [nums.index(target) , nums.index(target)]
#         return [-1 , -1]