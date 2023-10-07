class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left , right = 0 , len(skill)-1
        myhash = {}
        result =  0
        myhash[skill[left]+skill[right]] = left*right
        while left < right:
            result += skill[left]*skill[right]
            left +=1
            right-=1
            
            if skill[left] + skill[right] not in myhash:
                return -1
                
        return result
            