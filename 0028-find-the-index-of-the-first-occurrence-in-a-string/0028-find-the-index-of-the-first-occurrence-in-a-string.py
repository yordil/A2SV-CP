class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left , right =  0 , len(needle)
        
        for i in range(len(haystack)):
            if haystack[left:right] == needle:
                return i
            left +=1
            right +=1
            
        return -1