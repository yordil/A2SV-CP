class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mydict = Counter(s)
        myset = set()
        for i in mydict:
            myset.add(mydict[i])
        
        
        return True if len(myset) == 1 else False
            