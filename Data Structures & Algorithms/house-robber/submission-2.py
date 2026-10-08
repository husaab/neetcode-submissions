class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = 0

        memo = {}

        def rob_house(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob_current = nums[i] + rob_house(i+2)
            skip_current = rob_house(i+1)

            memo[i] = max(rob_current, skip_current)

            return memo[i]
        
        return rob_house(0)
        