class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        ans = [True] * len(candies)
        great = max(candies)
        j = 0
        for i in candies:
            if i + extraCandies < great:
                ans[j] = False
            
            j +=1
        return ans
                