class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()  # Sort the nums array to optimize the greedy approach

        result = []

        for query in queries:
            subsequence_size = 0
            remaining_sum = query

            for num in nums:
                if num <= remaining_sum:
                    subsequence_size += 1
                    remaining_sum -= num
                else:
                    break

            result.append(subsequence_size)

        return result
        