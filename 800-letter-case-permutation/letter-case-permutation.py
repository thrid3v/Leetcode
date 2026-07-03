class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(i, stri):
            if i == len(s):
                res.append(stri)
                return 
            if s[i].isalpha():
                dfs(i+1, stri + s[i].lower())

                dfs(i+1, stri + s[i].upper())
            else:
                dfs(i+1, stri + s[i])
        dfs(0,"")
        return res

        
        