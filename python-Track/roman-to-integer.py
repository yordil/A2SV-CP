class Solution:
    def romanToInt(self, s: str) -> int:
        hashtable = {
            "I": 1 , "V": 5 , "X": 10 , "L": 50 , "C": 100 , "D" : 500 , "M" : 1000
        }
        ans = 0
        for i in range(len(s)):
            if i+1 < len(s) and hashtable[s[i]] < hashtable[s[i+1]]:
                ans -= hashtable[s[i]]
            else:
                ans += hashtable[s[i]]

        return ans

# dawa









        
       