class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                current.append(nums[i])
                used[i] = True

                backtrack()

                current.pop()
                used[i] = False

        backtrack()
        return result