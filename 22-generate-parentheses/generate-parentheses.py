class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(res, curr, open, close, n):
            if len(curr) == 2*n:
                res.append(curr)
                return 
            if open < n:
                backtracking(res, curr+"(", open + 1, close, n)
            if close < open:
                backtracking(res, curr + ")", open, close + 1, n)
        backtracking(res, "", 0,0,n)
        return res
        
        
        