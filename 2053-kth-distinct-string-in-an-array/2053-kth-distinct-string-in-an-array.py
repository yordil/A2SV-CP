class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = 0 
        
        for i in arr:
            x =  arr.count(i)
            if x == 1:
                counter +=1
            if counter == k:
                return i
        return  ""
            