from functools import reduce
from operator import xor

class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        x = reduce(xor, nums, 0)

        if x:
            return n

        return n - 1 if any(nums) else 0