class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        po , ne , s = [] , [] , []
        
        
        
        for r in range(len(nums)):
            
            if nums[r] > 0: 
                po.append(nums[r]) 
            else: 
                ne.append(nums[r])
                    
        pos_pointer = 0
        neg_pointer = 0
        
        for r in range(len(nums)):
            if r % 2 == 0: 
                s.append(po[pos_pointer])
                pos_pointer +=1
            else:
                s.append(ne[neg_pointer])
                neg_pointer +=1
                
        return s
            
            
            
            