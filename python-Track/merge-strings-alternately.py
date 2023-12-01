class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        ans = ""
        l = 0
        r = 0
        while l < w1 and r < w2:
            ans +=word1[l]
            ans+=word2[r]
            l+=1
            r+=1

        if l != w1:
            while l <w1:
                ans+=word1[l]
                l+=1
        if r != w2:
            while r < w2:
                ans+= word2[r]
                r+=1

        return ans