from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        dq = deque()
        
        for l in range(n - 1, -1, -1):
            while dq and nums[dq[0]] <= nums[l]:
                curr = dq.popleft()
                nxt = dq[0] if dq else r + 1
                cost += (nxt - curr) * (nums[l] - nums[curr])
            
            dq.appendleft(l)
            
            while cost > k:
                cost -= nums[dq[-1]] - nums[r]
                if dq[-1] == r:
                    dq.pop()
                r -= 1
            
            ans += r - l + 1
            
        return ans