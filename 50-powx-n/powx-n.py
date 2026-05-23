class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        isnegative = False
        if n < 0:
            isnegative = True
            n = -n
        ans = 1.0
        while n > 0:
            if n % 2 == 0:
                x = x * x
                n = n // 2
            else:
                ans *= x
                n -= 1
        if isnegative == True:
            return 1 / ans
        else:
            return ans
        
        
        