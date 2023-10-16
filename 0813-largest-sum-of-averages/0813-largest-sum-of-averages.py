class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
    
        # Calculate the prefix sum for efficient average calculation
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

            # Initialize the dp array
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = prefix_sum[i] / i

        for i in range(1, n + 1):
            for j in range(2, k + 1):
                for x in range(i):
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix_sum[i] - prefix_sum[x]) / (i - x))

        return dp[n][k]

