class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 0
        fib = []
        while n1 <= n+1:
            if len(fib) == 0: fib.append(0)
            elif len(fib) == 1: fib.append(1)
            else: fib.append(fib[n1-2]+fib[n1-1])
            n1 += 1
        return fib[n+1]
