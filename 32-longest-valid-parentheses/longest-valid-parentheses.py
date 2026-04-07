class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = maxlen = 0

        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0    
        for c in reversed(s):
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2 * right)
            elif left > right:
                left = right = 0
        
        return maxlen
            

        