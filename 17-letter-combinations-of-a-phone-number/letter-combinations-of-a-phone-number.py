class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        combos = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(combos))
                return 
            for x in phone_map[digits[i]]:
                combos.append(x)
                dfs(i+1)
                combos.pop()
        dfs(0)
        return res

        