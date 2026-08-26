class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, char in enumerate(s) if char == '1']
        
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        result = ""
        
        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]
            current_len = right - left + 1
            current_sub = s[left : right + 1]
            
            if current_len < min_len:
                min_len = current_len
                result = current_sub
            elif current_len == min_len:
                if current_sub < result:
                    result = current_sub
                    
        return result