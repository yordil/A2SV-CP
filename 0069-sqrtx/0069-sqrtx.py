class Solution:
    def mySqrt(self, x: int) -> int:
        
        
        left= 0 
        right = x
        mid=0
        
        while left <= right:
            
            mid = left + ((right-left) // 2)
            
            if mid ** 2 > x:
                right = mid -1
            elif mid ** 2 < x:
                left = mid+1
                root = mid
            else:
                return mid
            
        return root