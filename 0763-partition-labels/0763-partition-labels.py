class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans= [ ]
        myhash = {}
        size = 0
        end = 0
#         create an array to count the last index
        for i, v in enumerate(s):
            myhash[v] = i
            
        for i , v in enumerate(s):
            size += 1
            end = max(end , myhash[v])
            
                      
                       
            if i == end:
                ans.append(size)
                size = 0
            
        return ans 
            
        
        