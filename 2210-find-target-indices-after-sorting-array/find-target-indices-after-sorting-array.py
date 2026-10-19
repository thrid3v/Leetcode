class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        nums.sort()
        for i, j in enumerate(nums):
            if j == target:
                res.append(i)
        return res

        