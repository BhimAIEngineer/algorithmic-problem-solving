from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        odd_chars = [char for char, freq in counts.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {char: freq // 2 for char, freq in counts.items() if freq // 2 > 0}
        m = n // 2
        
        def make_palindrome(half: str) -> str:
            if n % 2 == 1:
                return half + mid_char + half[::-1]
            return half + half[::-1]

        curr_counts = Counter(half_counts)
        prefix = []
        candidates = []

        for i in range(m + 1):
            if i < m:
                t_char = target[i]
                for c in sorted(curr_counts.keys()):
                    if c > t_char and curr_counts[c] > 0:
                        temp_counts = curr_counts.copy()
                        temp_counts[c] -= 1
                        suffix = "".join(sorted([ch * temp_counts[ch] for ch in temp_counts if temp_counts[ch] > 0]))
                        candidate_half = "".join(prefix) + c + suffix
                        candidates.append(candidate_half)
                
                if curr_counts[t_char] > 0:
                    prefix.append(t_char)
                    curr_counts[t_char] -= 1
                else:
                    break
            else:
                candidate_half = "".join(prefix)
                candidates.append(candidate_half)

        best = ""
        for cand_half in candidates:
            pal = make_palindrome(cand_half)
            if pal > target:
                if best == "" or pal < best:
                    best = pal

        return best