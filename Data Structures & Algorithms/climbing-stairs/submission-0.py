class Solution:
    def climbStairs(self, n: int) -> int:
        one_step_before = 1
        two_step_before = 1

        for _ in range(n):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current

        return two_steps_before