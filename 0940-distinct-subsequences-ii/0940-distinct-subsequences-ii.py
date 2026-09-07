class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = {}
        
        for char in s:
            prev_dp = dp
            dp = (2 * dp - last.get(char, 0)) % MOD
            last[char] = prev_dp
            
        return (dp - 1) % MOD