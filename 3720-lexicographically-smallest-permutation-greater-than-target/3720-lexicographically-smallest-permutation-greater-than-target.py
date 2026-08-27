from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        best_prefix_len = -1
        best_char_at_i = None
        
        for i in range(n):
            curr_char = target[i]
            
            for c in sorted(s_counts.keys()):
                if c > curr_char and s_counts[c] > 0:
                    best_prefix_len = i
                    best_char_at_i = c
                    break
            
            if s_counts[curr_char] > 0:
                s_counts[curr_char] -= 1
            else:
                break
        
        if best_prefix_len == -1:
            return ""
        
        res = []
        counts = Counter(s)
        
        for i in range(best_prefix_len):
            res.append(target[i])
            counts[target[i]] -= 1
            
        res.append(best_char_at_i)
        counts[best_char_at_i] -= 1
        
        for c in sorted(counts.keys()):
            if counts[c] > 0:
                res.append(c * counts[c])
                
        return "".join(res)