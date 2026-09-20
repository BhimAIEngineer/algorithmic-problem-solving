WEIGHTS = {chr(code): 123 - code for code in range(97, 123)}

class Solution:
    def reverseDegree(self, s: str) -> int:
        weights = WEIGHTS
        total = 0
        for i, char in enumerate(s, 1):
            total += weights[char] * i
        return total