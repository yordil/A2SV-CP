class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        answer =[]

        j = 0 #index for the first n numbers x s
        
        
        for i in range(n , len(nums)):
            answer.append(nums[j])
            answer.append(nums[i])
            j+=1
        return answer
            