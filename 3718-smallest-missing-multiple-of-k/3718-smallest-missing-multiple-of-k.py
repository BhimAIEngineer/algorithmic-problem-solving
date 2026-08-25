from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = set(nums)
        i = 1
        while True:
            candidate = i * k
            if candidate not in present:
                return candidate
            i += 1