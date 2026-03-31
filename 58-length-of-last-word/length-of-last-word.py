class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        x = len(s) - 1

        while x >= 0 and s[x] == " ":
            x -= 1
        while x >= 0 and s[x] != " ":
            counter += 1
            x -= 1
        return counter
