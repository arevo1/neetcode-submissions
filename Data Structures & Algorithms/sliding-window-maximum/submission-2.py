class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## Optimal Solution

        q = deque()
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if q[0] < r - k:
                q.popleft()
            
            if q[0] >= k - 1:
                res.append(nums[q[0]])
        return res