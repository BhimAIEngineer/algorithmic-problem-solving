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

        edge = [26 | (26 << 5)] * (size << 1)
        pre = [0] * (size << 1)
        suf = [0] * (size << 1)
        best = [0] * (size << 1)

        for i, c in enumerate(s):
            p = size + i
            x = ord(c) - 97
            edge[p] = x | (x << 5)
            pre[p] = suf[p] = best[p] = 1

        for p in range(size - 1, 0, -1):
            a = p << 1
            b = a | 1

            if best[a] == 0:
                edge[p] = edge[b]
                pre[p] = pre[b]
                suf[p] = suf[b]
                best[p] = best[b]
                continue

            if best[b] == 0:
                edge[p] = edge[a]
                pre[p] = pre[a]
                suf[p] = suf[a]
                best[p] = best[a]
                continue

            ea = edge[a]
            eb = edge[b]

            la = ea & 31
            ra = ea >> 5
            lb = eb & 31
            rb = eb >> 5

            edge[p] = la | (rb << 5)

            half = size >> p.bit_length()

            x = pre[a]
            if x == half and ra == lb:
                x += pre[b]
            pre[p] = x

            x = suf[b]
            if x == half and ra == lb:
                x += suf[a]
            suf[p] = x

            x = best[a] if best[a] > best[b] else best[b]

            if ra == lb:
                y = suf[a] + pre[b]
                if y > x:
                    x = y

            best[p] = x

        ans = []

        for c, idx in zip(queryCharacters, queryIndices):
            p = size + idx
            x = ord(c) - 97

            edge[p] = x | (x << 5)
            pre[p] = suf[p] = best[p] = 1

            p >>= 1
            half = 1

            while p:
                a = p << 1
                b = a | 1

                if best[a] == 0:
                    edge[p] = edge[b]
                    pre[p] = pre[b]
                    suf[p] = suf[b]
                    best[p] = best[b]

                elif best[b] == 0:
                    edge[p] = edge[a]
                    pre[p] = pre[a]
                    suf[p] = suf[a]
                    best[p] = best[a]

                else:
                    ea = edge[a]
                    eb = edge[b]

                    la = ea & 31
                    ra = ea >> 5
                    lb = eb & 31
                    rb = eb >> 5

                    edge[p] = la | (rb << 5)

                    x = pre[a]
                    if x == half and ra == lb:
                        x += pre[b]
                    pre[p] = x

                    x = suf[b]
                    if x == half and ra == lb:
                        x += suf[a]
                    suf[p] = x

                    x = best[a] if best[a] > best[b] else best[b]

                    if ra == lb:
                        y = suf[a] + pre[b]
                        if y > x:
                            x = y

                    best[p] = x

                p >>= 1
                half <<= 1

            ans.append(best[1])

        return ans