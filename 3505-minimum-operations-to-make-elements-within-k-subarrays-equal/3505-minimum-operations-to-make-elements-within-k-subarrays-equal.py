import heapq
import numpy as np

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        lo = []
        hi = []
        side = [0] * n
        lo_n = hi_n = 0
        lo_s = hi_s = 0
        target = (x + 1) // 2
        costs = []
        push = heapq.heappush
        pop = heapq.heappop

        for i in range(n):
            left = i - x + 1
            if i >= x:
                r = i - x
                if side[r] == 0:
                    lo_n -= 1
                    lo_s -= nums[r]
                else:
                    hi_n -= 1
                    hi_s -= nums[r]

            v = nums[i]
            while lo and lo[0][1] < left:
                pop(lo)
            if lo_n > 0 and v <= -lo[0][0]:
                push(lo, (-v, i))
                side[i] = 0
                lo_n += 1
                lo_s += v
            else:
                push(hi, (v, i))
                side[i] = 1
                hi_n += 1
                hi_s += v

            while lo_n > target:
                while lo[0][1] < left:
                    pop(lo)
                nv, j = pop(lo)
                nv = -nv
                lo_n -= 1
                lo_s -= nv
                push(hi, (nv, j))
                side[j] = 1
                hi_n += 1
                hi_s += nv
            while lo_n < target and hi_n > 0:
                while hi[0][1] < left:
                    pop(hi)
                nv, j = pop(hi)
                hi_n -= 1
                hi_s -= nv
                push(lo, (-nv, j))
                side[j] = 0
                lo_n += 1
                lo_s += nv

            if i >= x - 1:
                while lo[0][1] < left:
                    pop(lo)
                med = -lo[0][0]
                costs.append(med * lo_n - lo_s + hi_s - med * hi_n)

        costs = np.array(costs, dtype=np.int64)
        INF = 10 ** 18
        prev = np.zeros(n + 1, dtype=np.int64)
        for _ in range(k):
            cur = np.full(n + 1, INF, dtype=np.int64)
            cand = prev[: n - x + 1] + costs
            cur[x:] = np.minimum.accumulate(cand)
            prev = cur
        return int(prev[n])