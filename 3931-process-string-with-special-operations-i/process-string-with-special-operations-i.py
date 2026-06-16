class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] == "*":
                if res:
                    res.pop()
            elif s[i] == "#":
                res = res + res
            elif s[i] == "%":
                res = res[::-1]
            else:
                res.append(s[i])
        return "".join(res)

        