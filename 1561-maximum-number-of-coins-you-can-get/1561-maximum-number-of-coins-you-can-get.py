class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        maxpile=0
       
        # amount much pile each person get 
        pil = len(piles)/3
        # since it is sorted start from index pil then update by two since the maximum is taken by alice and us 
         
        for i in range (int(pil) , len(piles) , 2):
            maxpile+=piles[i]
            
        return maxpile