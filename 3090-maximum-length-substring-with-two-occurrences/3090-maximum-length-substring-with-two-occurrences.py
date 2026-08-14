class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = [0] * 26
        a = [ord(c) - 97 for c in s]
        left = ans = 0

        for right, x in enumerate(a):
            cnt[x] += 1

            while cnt[x] > 2:
                cnt[a[left]] -= 1
                left += 1

            length = right - left + 1
            if length > ans:
                ans = length

        return ans
