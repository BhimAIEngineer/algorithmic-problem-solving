class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = [0] * 26
        left = ans = 0

        for right in range(len(s)):
            i = ord(s[right]) - 97
            cnt[i] += 1

            while cnt[i] > 2:
                cnt[ord(s[left]) - 97] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
