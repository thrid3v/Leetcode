class Solution:
    def romanToInt(self, s: str) -> int:
        hashm = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and hashm[s[i]] < hashm[s[i + 1]]:
                res -= hashm[s[i]]
            else:
                res += hashm[s[i]]
        return res
