class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor = 0
        has_nonzero = False

        for x in nums:
            xor ^= x
            if x != 0:
                has_nonzero = True

        if xor != 0:
            return len(nums)

        return len(nums) - 1 if has_nonzero else 0