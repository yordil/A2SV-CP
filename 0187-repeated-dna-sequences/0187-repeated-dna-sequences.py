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
                
        
        
        