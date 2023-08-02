class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        hashset= set()
        dupl_pointer = 0
        Max=0
        
        for i in range(len(s)):
            while s[i] in hashset:
                hashset.remove(s[dupl_pointer])
                dupl_pointer+=1
           
            hashset.add(s[i])
            Max = max( Max, len(hashset))
            
        return Max
                      
        