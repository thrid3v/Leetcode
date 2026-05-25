class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(n):
            if n >= len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[n])
            dfs(n+1)
            subset.pop()
            while n + 1 < len(nums) and nums[n] == nums[n + 1]:
                n += 1
            dfs(n+1)
        dfs(0)
        return res

        