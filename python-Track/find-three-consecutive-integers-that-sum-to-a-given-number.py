class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid_no = num // 3
        if num % 3 != 0:
            return []
        
        return [mid_no -1 , mid_no , mid_no +1]