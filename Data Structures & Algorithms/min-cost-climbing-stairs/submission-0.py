class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)-1
        memo = {}
        def dp(n):

            if n>l:
                return 0
            if n in memo:
                return memo.get(n)
            else:
                c = (min(dp(n+1), dp(n+2)) + cost[n])
                memo[n] = c
                return c
        return min(dp(0), dp(1))

            