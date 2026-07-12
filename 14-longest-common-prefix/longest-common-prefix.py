class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        strs.sort()
        while i < len(strs[0]):
            if strs[0][i] == strs[len(strs)-1][i]:
                res += strs[0][i]
                i += 1
            else:
                i += 1
                break 
        return res


        