class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        lo, hi = min(s), max(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if s[0] == lo or s[-1] == hi:
            return 1
        if n == 2:
            return -1
        if s[-1] != lo or s.count(lo) > 1 or s[0] != hi or s.count(hi) > 1:
            return 2
        return 3