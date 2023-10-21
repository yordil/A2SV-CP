class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2
        return result















#  previous implmentation not efficient
# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
        
#         po , ne , s = [] , [] , []
        
        
        
#         for r in range(len(nums)):
            
#             if nums[r] > 0: 
#                 po.append(nums[r]) 
#             else: 
#                 ne.append(nums[r])
                    
#         pos_pointer = 0
#         neg_pointer = 1
        
#         for r in range(len(nums) , 2):
            
#             s.append(po[pos_pointer])
#             pos_pointer +=1
#                 s.append(ne[neg_pointer])
#                 neg_pointer +=1
                
#         return s
            
            
            
            