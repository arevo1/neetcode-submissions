class Solution:
    def trap(self, height: List[int]) -> int:
        max_l_arr = [0 if i==0 else max(height[:i]) for i in range(len(height))] 
        max_r_arr = [0 if i==(len(height)-1) else max(height[i+1:]) for i in range(len(height))]
        trap_w = 0
        for i in range(len(height)):
            trap_w += max((min(max_l_arr,max_r_arr)-height[i]),0)
        return trap_w