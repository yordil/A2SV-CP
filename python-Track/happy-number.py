class Solution:
    def isHappy(self, n: int) -> bool:
        myset = {2, 4, 8, 16, 37, 58, 89, 145, 42, 20}

        while n != 1:
            Sum = 0
            while n:
                Sum += (n % 10) ** 2
                n //= 10

            if Sum in myset:
                return False

            n = Sum

        return True
