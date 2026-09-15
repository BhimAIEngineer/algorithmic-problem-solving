class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans = 0
        last = 0
        n = len(s)
        
        for i in range(n):
            if i - k + 1 >= last and s[i - k + 1 : i + 1] == s[i - k + 1 : i + 1][::-1]:
                ans += 1
                last = i + 1
            elif i - k >= last and s[i - k : i + 1] == s[i - k : i + 1][::-1]:
                ans += 1
                last = i + 1
                
        return ans