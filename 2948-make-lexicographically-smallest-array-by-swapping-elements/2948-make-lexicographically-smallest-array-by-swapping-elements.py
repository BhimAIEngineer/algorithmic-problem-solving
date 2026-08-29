class Solution:

  def lexicographicallySmallestArray(
      self, nums: list[int], limit: int
  ) -> list[int]:
    n = len(nums)
    indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))

    res = [0] * n
    i = 0
    while i < n:
      j = i
      while j < n - 1 and indexed_nums[j + 1][0] - indexed_nums[j][0] <= limit:
        j += 1

      group = indexed_nums[i : j + 1]
      values = [item[0] for item in group]
      indices = [item[1] for item in group]

      indices.sort()

      for idx, val in zip(indices, values):
        res[idx] = val

      i = j + 1

    return res