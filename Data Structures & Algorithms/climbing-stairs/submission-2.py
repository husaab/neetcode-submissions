class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in memo:
                return memo[n]
            
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]

        return climb(n)