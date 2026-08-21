from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        useful = []

        for c in coins:
            if not any(c % x == 0 for x in useful):
                useful.append(c)

        n = len(useful)
        size = 1 << n
        lcms = [1] * size

        for mask in range(1, size):
            bit = mask & -mask
            i = bit.bit_length() - 1
            prev = mask ^ bit
            lcms[mask] = lcms[prev] // gcd(lcms[prev], useful[i]) * useful[i]

        def count(x):
            total = 0

            for mask in range(1, size):
                lcm = lcms[mask]

                if lcm <= x:
                    v = x // lcm
                    if mask.bit_count() & 1:
                        total += v
                    else:
                        total -= v

            return total

        lo = 1
        hi = useful[0] * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo