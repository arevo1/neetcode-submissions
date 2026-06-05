class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i
                maxA = max(maxA, height * width)
            stack.append(i)
        n = len(heights)

        while stack:
            height = heights[stack.pop()]
            if stack:
                width = n - stack[-1] -1
            else:
                width = n
            maxA = max(maxA, height * width)
        return maxA
