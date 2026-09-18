class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        answer = float('inf')
        min_len = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != float('inf'):
                    answer = min(answer, length + best[left - 1])

                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if answer == float('inf') else answer
