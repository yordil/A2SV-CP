class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = {j[0]:i for (i,j) in enumerate(intervals)}
        sort = sorted(list(start.keys()))
        res = []

        def binary_search(value,temp):
            low, high = 0, len(start)-1
            while low<=high:
                mid = (low+high)//2
                if sort[mid]>=value:
                    temp = start[sort[mid]]
                    high = mid-1
                else:
                    low = mid+1
            return temp

        for i in range(len(intervals)):
            res.append(binary_search(intervals[i][1],-1))
        return res