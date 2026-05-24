class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even = ceil(n / 2)
        odd = n // 2

        def poww(x, n):
            res = 1
            while n > 0:
                if n % 2 == 0:
                    x = (x * x) % MOD
                    n = n / 2
                elif n % 2 != 0:
                    res = (res * x) % MOD
                    n -= 1
            return res

        return (poww(5, even) * poww(4, odd)) % MOD

         
        