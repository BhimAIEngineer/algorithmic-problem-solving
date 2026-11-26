class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 0
        stones = 10
        while n >= stones and stones > 0:
            n -= stones
            stones -= 1
            turn += 1
        return turn % 2 == 1