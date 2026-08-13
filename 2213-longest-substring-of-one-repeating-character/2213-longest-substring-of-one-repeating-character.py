from typing import List

class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)

        left = [''] * (4 * n)
        right = [''] * (4 * n)
        prefix = [0] * (4 * n)
        suffix = [0] * (4 * n)
        best = [0] * (4 * n)
        length = [0] * (4 * n)

        def merge(node):
            l = node * 2
            r = l + 1

            left[node] = left[l]
            right[node] = right[r]
            length[node] = length[l] + length[r]

            prefix[node] = prefix[l]
            if prefix[l] == length[l] and right[l] == left[r]:
                prefix[node] += prefix[r]

            suffix[node] = suffix[r]
            if suffix[r] == length[r] and right[l] == left[r]:
                suffix[node] += suffix[l]

            best[node] = max(best[l], best[r])

            if right[l] == left[r]:
                best[node] = max(
                    best[node],
                    suffix[l] + prefix[r]
                )

        def build(node, start, end):
            if start == end:
                c = s[start]
                left[node] = c
                right[node] = c
                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                length[node] = 1
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            merge(node)

        def update(node, start, end, index, char):
            if start == end:
                left[node] = char
                right[node] = char
                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(best[1])

        return ans