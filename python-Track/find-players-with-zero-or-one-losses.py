from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        hashlose = set()
        hashwin = set()
        lose_ans = set()
        
        for i in matches:
            win , lose = i
            
            hashwin.add(win)
            
            if lose in hashlose:
                lose_ans.discard(lose)
            else:
                lose_ans.add(lose)
            
            hashlose.add(lose)
            
        winners = list(hashwin.difference(hashlose))
        losers = list(lose_ans)
        
        winners.sort()
        
        losers.sort()
        
        return [winners , losers]
                
        
#      since the answer should be in sorted order complexity will be O(NlogN)
    
            
            
                