class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hgts=sorted(heights,reverse=True)
        p=[]
        for i in hgts:
            p.append(names[heights.index(i)])
        return p
            