from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        for length in range(l, r + 1):
            curr_sum = sum(nums[:length])
            if curr_sum > 0:
                min_sum = min(min_sum, curr_sum)
                
            for i in range(length, n):
                curr_sum += nums[i] - nums[i - length]
                if curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)
                    
        return min_sum if min_sum != float('inf') else -1