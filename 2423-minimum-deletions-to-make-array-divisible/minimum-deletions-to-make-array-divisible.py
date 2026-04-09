class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        x = math.gcd(*numsDivide)

        nums.sort()

        for i, j in enumerate(nums):
            if x % j == 0:
                return i

        return -1
