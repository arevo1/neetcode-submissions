class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_a = 0

        while l<r:
            w = r-l
            c_h = min(heights[l],heights[r])
            a = c_h * w
            max_a = max(max_a, a)

            if heights[l]<heights[r]:
                l += 1
            else:
                r -= 1 
        return max_a