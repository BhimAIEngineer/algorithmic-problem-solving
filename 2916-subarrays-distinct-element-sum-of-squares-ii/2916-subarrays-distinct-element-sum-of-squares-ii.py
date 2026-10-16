class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        b1 = [0] * (n + 2)
        b2 = [0] * (n + 2)

        def upd(b, i, v):
            while i <= n + 1:
                b[i] += v
                i += i & -i

        def qry(b, i):
            s = 0
            while i > 0:
                s += b[i]
                i -= i & -i
            return s

        def range_add(l, r, v):
            upd(b1, l, v)
            upd(b1, r + 1, -v)
            upd(b2, l, v * (l - 1))
            upd(b2, r + 1, -v * r)

        def prefix(x):
            return qry(b1, x) * x - qry(b2, x)

        last = {}
        cur = 0
        ans = 0
        for j in range(1, n + 1):
            x = nums[j - 1]
            p = last.get(x, 0)
            l, r = p + 1, j
            s = prefix(r) - prefix(l - 1)
            cur += 2 * s + (r - l + 1)
            range_add(l, r, 1)
            last[x] = j
            ans += cur
        return ans % MOD