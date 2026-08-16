class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        from bisect import bisect_right

        n = len(stoneValue)

        if n == 1:
            return 0

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]

        for i in range(n):
            left[i][i] = stoneValue[i]
            right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] + prefix[i]

                p = bisect_right(
                    prefix,
                    total // 2,
                    i + 1,
                    j + 1
                ) - 1

                best = 0

                # Left sum <= right sum
                if p >= i + 1:
                    best = left[i][p - 1]

                # Right sum <= left sum
                start = p

                if 2 * prefix[p] < total:
                    start += 1

                start = max(start, i + 1)

                if start <= j:
                    best = max(best, right[start][j])

                dp[i][j] = best

                current = dp[i][j] + prefix[j + 1] - prefix[i]

                left[i][j] = max(left[i][j - 1], current)
                right[i][j] = max(right[i + 1][j], current)

        return dp[0][n - 1]