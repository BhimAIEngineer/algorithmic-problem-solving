class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        ans = 0
        for i in range(1000, n + 1):
            ans += len(str(i)) // 4
        return ans
