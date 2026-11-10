class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for k in range(1, min(3, i) + 1):
                jump_cost = costs[i - 1] + k * k
                dp[i] = min(dp[i], dp[i - k] + jump_cost)
                
        return dp[n]