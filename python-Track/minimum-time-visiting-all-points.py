class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        S = 0
        for i in range(len(points)-1):
            p , q = points[i]
            r , s = points[i+1]
            # p =  abs(p)
            # q = abs(q)
            # r = abs(r)
            # s = abs(s)

            S += max(abs(r-p) , abs(s-q))
        return S 