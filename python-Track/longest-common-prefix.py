class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        
        small_str = "0" * 202
        for i in strs:
            if len(i) < len(small_str):
                small_str = i
        ans =  str(small_str)
      
        for i in range(len(strs)):
            for j in range(len(small_str)):
                    temp = strs[i]
                    if temp[j] == small_str[j]:
                        continue
                    elif j < len(ans):
                        ans = small_str[:j]

        return ans

            

