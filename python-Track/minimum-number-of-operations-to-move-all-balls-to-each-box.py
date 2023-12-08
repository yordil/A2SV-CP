from collections import defaultdict
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        # a = list(boxes)
#       collector for key 0 or 1 and their corresponding index as a list of value
        
        for i in range(len(boxes)):
            S = 0
            for j in range(len(boxes)):
                
                if boxes[j] == "1":
                    S += abs(i-j)
                    
            ans[i]  = S
        return ans
                
    
    
    
#         hashmap = defaultdict(list)
        
#         for i in range(len(boxes)):
            
#             if int(i):
#                 hashmap.append(i)
        
#         for i in range(len(boxes)):
            
#             if 
        
        
            
            
            