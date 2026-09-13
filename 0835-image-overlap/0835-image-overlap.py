class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = []
        b = []

        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    a.append((i, j))
                if img2[i][j]:
                    b.append((i, j))

        shifts = {}

        for x1, y1 in a:
            for x2, y2 in b:
                shift = (x2 - x1, y2 - y1)
                shifts[shift] = shifts.get(shift, 0) + 1

        return max(shifts.values(), default=0)
