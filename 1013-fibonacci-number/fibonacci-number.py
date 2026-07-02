class Solution:
    def fib(self, n: int) -> int:
        #this is the bottom up solution or the tabulation solution with constant space 
        if n == 0:
            return 0
        if n == 1:
            return 1 
        prev, curr = 0,1
        for i in range(2,n+1):
            prev, curr = curr, curr + prev
        return curr
        