class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}
        maxlen, count = 0, 0

        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1

            if count in count_map:
                maxlen = max(maxlen, i - count_map[count])
            else:
                count_map[count] = i

        return maxlen

        