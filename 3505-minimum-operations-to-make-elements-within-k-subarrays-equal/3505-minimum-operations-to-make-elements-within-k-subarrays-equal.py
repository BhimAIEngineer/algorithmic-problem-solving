class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        idx = {v: i + 1 for i, v in enumerate(vals)}
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(i, c, s):
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        top = 1
        while top * 2 <= m:
            top *= 2

        def kth(t):
            pos = 0
            rem = t
            pw = top
            while pw:
                nxt = pos + pw
                if nxt <= m and cnt[nxt] < rem:
                    pos = nxt
                    rem -= cnt[nxt]
                pw >>= 1
            return pos + 1

        target = (x + 1) // 2
        costs = []
        total = 0
        for i in range(n):
            update(idx[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                old = nums[i - x]
                update(idx[old], -1, -old)
                total -= old
            if i >= x - 1:
                p = kth(target)
                med = vals[p - 1]
                c, s = prefix(p)
                costs.append(med * c - s + (total - s) - med * (x - c))

        INF = float("inf")
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                best = cur[i - 1]
                cand = prev[i - x] + costs[i - x]
                if cand < best:
                    best = cand
                cur[i] = best
            prev = cur
        return prev[n]