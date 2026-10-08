class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ob = '('
        cb = ')'
        cnt = 0
        res = ""
        for i in range(len(s)):
            if s[i] == ob:
                if cnt != 0:
                    res += s[i]
                cnt += 1
            if s[i] == cb:
                cnt -= 1
                if cnt != 0:
                    res += s[i]
        return res
                


                
                    

            
