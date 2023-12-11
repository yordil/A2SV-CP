class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        more = 0.25 * len(arr)
        ans  = Counter(arr)
        
        for i in ans:
            if ans[i] > more:
                return i
        return 0
            
        
        
        