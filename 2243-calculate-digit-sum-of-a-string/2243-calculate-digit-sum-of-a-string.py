class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = []
            for i in range(0, len(s), k):
                group_sum = sum(int(ch) for ch in s[i:i + k])
                groups.append(str(group_sum))
            s = "".join(groups)
        return s