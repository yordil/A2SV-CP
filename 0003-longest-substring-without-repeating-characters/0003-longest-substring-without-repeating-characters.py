class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashset = set()

        ans = 0

        l = 0

        for r in range(len(s)):
            if s[r] in hashset:
                while l < r and  s[r] in hashset:
                    hashset.remove(s[l])
                    l+=1

            hashset.add(s[r])

            ans = max(ans , len(hashset))

        return ans 

    



