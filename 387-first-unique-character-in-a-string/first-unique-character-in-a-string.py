class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashm = {}

        for i in range(len(s)):
            hashm[s[i]] = 1 + hashm.get(s[i],0)
        
        for i in range(len(s)):
            if hashm[s[i]] == 1:
                return i
                
        return -1 
        