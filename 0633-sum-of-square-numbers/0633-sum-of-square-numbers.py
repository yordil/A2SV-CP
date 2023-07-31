#from math import ceil
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0 
        right =ceil(sqrt(c))
      
        while left <= right :
            if left*left + right*right == c :
                return True
            elif left*left + right*right > c :
                right -= 1
            elif left*left + right*right < c :
                left +=1
       
        return False