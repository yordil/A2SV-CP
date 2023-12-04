class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        ans = []
        arr = s.split()
        l = 0   
        for i in arr:
            l = max(len(i) , l)

        for i in range(l):
            temp = []
            for word in arr:
                if i < len(word):
                    temp.append(word[i])
                else:
                    temp.append(" ")
            
            ans.append("".join(temp).rstrip())

        return ans

