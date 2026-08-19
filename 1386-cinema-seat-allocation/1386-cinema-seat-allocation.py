from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved[row].add(seat)
        
        ans = (n - len(reserved)) * 2
        
        for row, seats in reserved.items():
            left = not (seats & {2, 3, 4, 5})
            right = not (seats & {6, 7, 8, 9})
            middle = not (seats & {4, 5, 6, 7})
            
            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1
                
        return ans