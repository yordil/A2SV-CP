class Solution:
    def findWords(self, words: List[str]) -> List[str]:
    
        hashlist = [ "qwertyuiop" , "asdfghjkl"  , "zxcvbnm"]
        ans = []
        for i in range(len(words)):
            j = 0
            temp = words[i]
            idx = 0
            if temp[0].lower() in hashlist[0]:
                idx  = 0
            elif temp[0].lower() in hashlist[1]:
                idx = 1
            else:
                idx = 2
            while j < len(temp):
                if temp[j].lower() not in hashlist[idx]:
                    break
                j+=1
            else:
                ans.append(words[i])

        return ans 

