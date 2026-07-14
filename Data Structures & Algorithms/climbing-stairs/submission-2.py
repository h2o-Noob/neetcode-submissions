class Solution:
    def climbStairs(self, n: int) -> int:
        sums = {}
        def dp(n):


            if n<0:
                return 0
            elif n == 0:
                return 1
            else:
                if n in sums:
                    return sums.get(n)
                sum = dp(n-1) + dp(n-2)
                sums[n] = sum
                return sum
        
        return dp(n)

        