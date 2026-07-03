class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []
        def dfs(start):
            if len(sol) == k:
                res.append(sol[:])
                return 
            for i in range(start, n+1):
                sol.append(i)
                dfs(i+1)
                sol.pop()
        dfs(1)
        return res

        