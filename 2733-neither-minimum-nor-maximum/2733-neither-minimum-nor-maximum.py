class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nset = set(nums)
        mlist =list(nset)
        if(len(mlist) < 3):
            return -1
        else:
            flist = sorted(mlist)
            return flist[1]
            