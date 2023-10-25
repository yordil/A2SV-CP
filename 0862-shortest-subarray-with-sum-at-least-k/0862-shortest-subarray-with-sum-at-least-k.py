from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_len = n + 1  # Initialize min_len to a value greater than the array size
        prefix_sum = [0] * (n + 1)  # Store prefix sum

        # Calculate the prefix sum
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Use a deque to keep track of potential subarrays that meet the condition
        dq = deque()

        for i in range(n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())

            # Keep elements in the deque that might be useful for future calculations
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return min_len if min_len <= n else -1
