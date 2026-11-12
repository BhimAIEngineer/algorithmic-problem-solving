class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        best = inc = dec = 1
        prev = nums[0]
        for x in nums[1:]:
            if x > prev:
                inc += 1
                dec = 1
                if inc > best:
                    best = inc
            elif x < prev:
                dec += 1
                inc = 1
                if dec > best:
                    best = dec
            else:
                inc = dec = 1
            prev = x
        return best