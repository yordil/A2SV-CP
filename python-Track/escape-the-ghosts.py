class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        distsum = abs(target[0])  + abs(target[1])

        for i in ghosts:
            a , b  = i
            
            
            if abs(target[1] - b) + abs((target[0] - a)) <= distsum:
                return False
        return True