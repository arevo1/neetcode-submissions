class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = 0
        max_r = 0
        trap_w = 0
        l = 0
        r = len(height)-1

        while l<r:
            if height[l]<height[r]:
                trap_w += max(min(height[l],max_l)-height[l],0)
                l+=1
            else:
                trap_w += max(min(height[r],max_r)-height[r],0)
                r-=1
        return trap_w

