class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxi = 0
        charset = set()
        for x in range(len(s)):
            while s[x] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[x])
            maxi = max(maxi, x - l + 1)
        return maxi
