class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        left , right  =  0 , len(s) -1
        ss = list(s)
        while left <= right:

            if ss[left].isalpha() and ss[right].isalpha():
                ss[left] , ss[right] = ss[right] , ss[left]
                left+=1
                right-=1
            elif ss[left].isalpha() and not ss[right].isalpha():
                right -=1
            elif not ss[left].isalpha() and ss[right].isalpha():
                left +=1
            else:
                left+=1
                right -=1
                
        return ''.join(ss)
                