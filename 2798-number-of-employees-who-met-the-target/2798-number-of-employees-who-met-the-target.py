class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        return len(hours) - bisect_left(hours , target)