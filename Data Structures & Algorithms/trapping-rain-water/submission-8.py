class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = 0
        max_r = 0
        trap_w = 0
        l = 0
        r = len(height)-1

        while l<r:
            if height[l]<height[r]:
                trap_w += (max_l:=max(height[l],max_l))-height[l]
                l+=1
            else:
                trap_w += (max_r:=max(height[r],max_r))-height[r]
                r-=1
        return trap_w

