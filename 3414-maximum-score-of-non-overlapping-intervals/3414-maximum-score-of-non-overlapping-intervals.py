from bisect import bisect_right
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: (x[0], x[3])
        )

        starts = [x[0] for x in arr]

        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):
                best_score, best_indices = dp[k][i + 1]

                l, r, w, idx = arr[i]
                j = next_idx[i]

                take_score, take_indices = dp[k - 1][j]
                take_score += w
                take_indices = tuple(sorted((idx,) + take_indices))

                if (take_score > best_score or
                    (take_score == best_score and take_indices < best_indices)):
                    dp[k][i] = (take_score, take_indices)
                else:
                    dp[k][i] = (best_score, best_indices)

        return list(dp[4][0][1])
