class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        moves = 0

        for ch in s:
            if ch == '(':
                balance += 1
            elif balance > 0:
                balance -= 1
            else:
                moves += 1

        return moves + balance
