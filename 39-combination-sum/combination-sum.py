class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        csum = []    
        def dfs(i, t):
            if t == target:
                res.append(csum.copy())
                return 
            if t > target or i == len(candidates):
                return 
            
            csum.append(candidates[i])
            dfs(i,t + candidates[i])

            csum.pop()
            dfs(i + 1, t)
        dfs(0,0)
        return res
        