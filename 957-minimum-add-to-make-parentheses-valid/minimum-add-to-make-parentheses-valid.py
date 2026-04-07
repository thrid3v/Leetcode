class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0
        for c in s:
            if c == "(":
                close_needed += 1
            else:
                close_needed -= 1
            if close_needed < 0:
                open_needed += 1
                close_needed = 0
        return close_needed + open_needed
