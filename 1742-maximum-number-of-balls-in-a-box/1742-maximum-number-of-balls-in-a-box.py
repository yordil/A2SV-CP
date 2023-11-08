class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        myhash = {}
        max_count = 0
        
        for i in range(lowLimit, highLimit + 1):  # Include highLimit in the range
            num = i
            num2 = 0  # Initialize the variable to calculate the sum of digits
            
            while num:
                num2 += num % 10
                num //= 10  # Use integer division to get the next digit
            
            if num2 not in myhash:
                myhash[num2] = 1
            else:
                myhash[num2] += 1  # Increment the count for the sum of digits
            
            max_count = max(max_count, myhash[num2])  # Update the maximum count
        
        return max_count

                
            