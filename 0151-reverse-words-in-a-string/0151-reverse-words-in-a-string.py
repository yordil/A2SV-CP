class Solution:
    def reverseWords(self, s: str) -> str:
        s.split() 
        words = s.split() 
        out = []
        for k in range(len(words) - 1 , -1 , -1):
            out.append(words[k])
        return ' '.join(out)  