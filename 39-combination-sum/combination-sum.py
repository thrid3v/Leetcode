class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        csum = []
        nums = candidates 
        
        def dfs(i, t):
            if t == target:
                res.append(csum.copy())
                return 
            if t > target or i == len(nums):
                return 
            
            csum.append(nums[i])
            dfs(i,t + nums[i])

            csum.pop()
            dfs(i + 1, t)
        dfs(0,0)
        return res
        