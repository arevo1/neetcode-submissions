class Solution:
    def trap(self, height: List[int]) -> int:
        ## forced to tle by 1 unfair test case on leetcode against the fabric of python, no matter the serpent adapts;
        max_l = 0
        max_r = 0
        max_l_arr = [(prev := max_l, max_l := max(max_l,h))[0] for h in height]
        max_r_arr = [(prev := max_r, max_r := max(max_r,h))[0] for h in height[::-1]][::-1]
        trap_w = 0
        for i in range(len(height)):
            trap_w += max((min(max_l_arr[i],max_r_arr[i])-height[i]),0)
        return trap_w
