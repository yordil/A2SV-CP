class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        flag1 = False
        flag2 = False
        
        set1 = set(range(left, right+1))
        set2 = set()
        for i in ranges:
            a , b  = i
            temp = list(range(a, b+1))
            set2.update(temp)
            
            
        return set1 <= set2
            
            