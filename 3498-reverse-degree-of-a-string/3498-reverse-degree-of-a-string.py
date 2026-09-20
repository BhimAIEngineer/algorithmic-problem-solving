class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((ord('z') - ord(char) + 1) * i for i, char in enumerate(s, 1))