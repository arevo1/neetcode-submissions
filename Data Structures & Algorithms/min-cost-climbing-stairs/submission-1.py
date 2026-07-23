class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, 0

        for current_cost in cost:
            current = current_cost + min(prev1, prev2)
            prev2 = prev1
            prev1 = current

        return min(prev1, prev2)
