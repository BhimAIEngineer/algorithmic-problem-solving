class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                if first_cp == -1:
                    first_cp = index
                if prev_cp != -1:
                    min_dist = min(min_dist, index - prev_cp)
                prev_cp = index
            
            prev = curr
            curr = curr.next
            index += 1
        
        if first_cp == prev_cp:
            return [-1, -1]
        
        return [min_dist, prev_cp - first_cp]