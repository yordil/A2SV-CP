class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        myhash = set()
        l = 0
        ans = 0 

        for i in range(len(s)):
            while l < i and  s[i] in myhash:
                myhash.remove(s[l])
                l+=1
            myhash.add(s[i])

            ans  = max(ans , len(myhash))

        return ans 

