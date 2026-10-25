class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashm = {}
        for i in text:
            hashm[i] = hashm.get(i,0) + 1
        
        return min(
            hashm.get('b',0),
            hashm.get('a',0),
            hashm.get('l',0) // 2,
            hashm.get('o',0) // 2,
            hashm.get('n',0)
        )


        