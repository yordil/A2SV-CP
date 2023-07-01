class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        tot = sum(salary)
        tot -=salary[0] + salary[len(salary)-1]
        x =len(salary)-2
        return tot/x
       