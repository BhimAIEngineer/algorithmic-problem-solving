from typing import List

class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        size = 1

        while size < n:
            size <<= 1

        lc = [26] * (2 * size)
        rc = [26] * (2 * size)
        pre = [0] * (2 * size)
        suf = [0] * (2 * size)
        best = [0] * (2 * size)
        ln = [0] * (2 * size)

        for i, c in enumerate(s):
            p = size + i
            x = ord(c) - 97
            lc[p] = rc[p] = x
            pre[p] = suf[p] = best[p] = ln[p] = 1

        for p in range(size - 1, 0, -1):
            a = p << 1
            b = a | 1

            ln[p] = ln[a] + ln[b]
            lc[p] = lc[a]
            rc[p] = rc[b]

            x = pre[a]
            if x == ln[a] and rc[a] == lc[b]:
                x += pre[b]
            pre[p] = x

            x = suf[b]
            if x == ln[b] and rc[a] == lc[b]:
                x += suf[a]
            suf[p] = x

            x = best[a]
            if best[b] > x:
                x = best[b]

            if rc[a] == lc[b]:
                y = suf[a] + pre[b]
                if y > x:
                    x = y

            best[p] = x

        ans = []

        for c, idx in zip(queryCharacters, queryIndices):
            p = size + idx
            x = ord(c) - 97

            lc[p] = rc[p] = x
            pre[p] = suf[p] = best[p] = ln[p] = 1

            p >>= 1

            while p:
                a = p << 1
                b = a | 1

                ln[p] = ln[a] + ln[b]
                lc[p] = lc[a]
                rc[p] = rc[b]

                x = pre[a]
                if x == ln[a] and rc[a] == lc[b]:
                    x += pre[b]
                pre[p] = x

                x = suf[b]
                if x == ln[b] and rc[a] == lc[b]:
                    x += suf[a]
                suf[p] = x

                x = best[a]
                if best[b] > x:
                    x = best[b]

                if rc[a] == lc[b]:
                    y = suf[a] + pre[b]
                    if y > x:
                        x = y

                best[p] = x
                p >>= 1

            ans.append(best[1])

        return ans