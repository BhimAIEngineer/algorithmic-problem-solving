
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            return (
                comb[len(left) + len(right)][len(left)]
                * solve(left) % MOD
                * solve(right) % MOD
            )

        return (solve(nums) - 1) % MOD
