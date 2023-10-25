class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        myhash = {}
        
        arr = []
        Str = s[0:10]
        L = 1
        for i in range(10 ,len(s)+1):
            if Str not in myhash:
                myhash[Str] = 1
            elif Str not in arr:
                arr.append(Str)
                
            Str = s[L:i+1]
            L+=1
        return arr
                
        
#         ans , visit  = set() , set()
#         Str = ""
        
#         for l in range(len(s) -9):
#             Str = s[l:l+10]
#             if Str in visit:
#                 ans.add(Str)
#             else:
#                 visit.add(Str)
                
#         return list(ans)
    
        
        
        

