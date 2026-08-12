from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = ans = 0

        for right, x in enumerate(nums):
            freq[x] += 1

            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1

            length = right - left + 1
            if length > ans:
                ans = length

        return ans