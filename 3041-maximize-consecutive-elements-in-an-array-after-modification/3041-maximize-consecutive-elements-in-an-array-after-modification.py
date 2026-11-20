from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        
        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            
        return max(dp.values())