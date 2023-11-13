class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        maxc = 0
        hashtable = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
        cursum = 0
        for i in range(len(s)):
            
            cursum = max(cursum , 0)
            
            if s[i] in chars:
                idx = chars.index(s[i])
                cursum += vals[idx]
            else:
                cursum += hashtable[s[i]]
            
            
            if cursum > maxc:
                maxc = cursum
                
        return maxc
            