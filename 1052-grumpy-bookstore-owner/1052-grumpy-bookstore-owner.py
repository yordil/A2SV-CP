class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        grump =  False

        window = minutes
        left = 0
        answer  = 0
        oneprefix =  0
        tempans  = 0
        maxx = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                oneprefix +=1
                tempans += customers[i]
            if grumpy[i] == 0:
                answer += customers[i]
            if i >= minutes - 1:
                maxx = max(tempans , maxx)
                if grumpy[left] == 1:
                    oneprefix -=1
                    tempans -= customers[left]
                left+=1
        return answer + maxx
            
            
            