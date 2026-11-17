class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        cost = [[float('inf')] * n for _ in range(n)]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                sub = s[i:j+1]
                min_changes = float('inf')
                
                for d in divisors[length]:
                    current_changes = 0
                    for r in range(d):
                        group = [sub[idx] for idx in range(r, length, d)]
                        l_g = len(group)
                        for x in range(l_g // 2):
                            if group[x] != group[l_g - 1 - x]:
                                current_changes += 1
                    min_changes = min(min_changes, current_changes)
                cost[i][j] = min_changes

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for p in range(1, min(k, i) + 1):
                for m in range(p - 1, i):
                    if dp[m][p - 1] != float('inf') and cost[m][i - 1] != float('inf'):
                        dp[i][p] = min(dp[i][p], dp[m][p - 1] + cost[m][i - 1])
                        
        return dp[n][k]