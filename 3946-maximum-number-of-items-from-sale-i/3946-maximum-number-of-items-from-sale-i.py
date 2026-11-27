class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        gain1 = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 1
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            gain1[i] = cnt

        order = sorted(range(n), key=lambda i: items[i][1], reverse=True)
        neg_inf = -10**9
        dp = [neg_inf] * (budget + 1)
        dp[0] = 0
        ans = 0

        for i in order:
            pi = items[i][1]
            g = gain1[i]

            if pi <= budget:
                for prev_c in range(budget - pi + 1):
                    if dp[prev_c] >= 0:
                        total_c = prev_c + pi
                        rem = budget - total_c
                        cur = dp[prev_c] + g + (rem // pi)
                        if cur > ans:
                            ans = cur

            for c in range(budget, pi - 1, -1):
                if dp[c - pi] + g > dp[c]:
                    dp[c] = dp[c - pi] + g

        return ans