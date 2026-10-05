class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        return [x for x in range(min(nums), max(nums) + 1) if x not in nums_set]
