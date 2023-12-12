class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # ans = [0] * len(queries)
        sum_of_even =0
        ans = []
        for i in nums:
            if i%2 == 0:
                sum_of_even += i
        
        print(sum_of_even)
        
        for q in queries:
            val , index = q
            
            current_sum = nums[index] + val
            
            if nums[index] % 2 != 0 and current_sum  % 2 == 0 :
                sum_of_even += current_sum
            elif current_sum  % 2 != 0 and nums[index] %2 == 0:
                sum_of_even -= nums[index]
            elif current_sum  % 2 == 0 and nums[index] %2 == 0:
                sum_of_even += val
            
            nums[index] = current_sum
            ans.append(sum_of_even)
           
        return ans
                
            
        
        